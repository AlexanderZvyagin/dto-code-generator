import json, yaml, logging, copy
from enum import StrEnum, auto

from cgdto import *

logger = logging.getLogger(__name__)

def schema_version () -> str:
    return 'OpenApi schema (0.1.0)'

class OpenApiBasicType(StrEnum):
    null        = auto()
    boolean     = auto()
    number      = auto()
    integer     = auto()
    string      = auto()

class OpenApiDependentType(StrEnum):
    array       = auto()
    object      = auto()
    anyOf       = auto()

class OpenApiType(StrEnum):
    _ignore_ = 'member cls'
    cls = vars()
    for member in list(OpenApiBasicType)+list(OpenApiDependentType):
        cls[member.name] = member.value

class OpenApiFormat(StrEnum):
    none  = ''
    int32 = auto()
    int64 = auto()

def mapOpenapiType(type:str,format:str='',name='') -> Variable:
    if format:
        logger.warning(f'openapiFormat="{format}" is ignored')
    match type:
        case OpenApiType.null:
            return Variable(name=name,type=BasicType.null)
        case OpenApiType.boolean:
            return Variable(name=name,type=BasicType.boolean)
        case OpenApiType.number:
            return Variable(name=name,type=BasicType.float)
        case OpenApiType.integer:
            return Variable(name=name,type=BasicType.int)
            # match openapiFormat:
            #     case OpenApi.Format.none: return 'int'
            #     case OpenApi.Format.int32: return 'int'
            #     case OpenApi.Format.int64: return 'int'
            #     case _: raise Exception(f'{self.langName} unsupported type={openapiType} format={openapiFormat}')
        case OpenApiType.string:
            return Variable(name=name,type=BasicType.string)
        case OpenApiType.array:
            return Variable(name=name,type=BasicType.null,list=True)
            # return BasicType.string
            # match openapiFormat:
            #     case '': return 'std::string'
            #     case _: raise Exception(f'{self.langName} unsupported type={openapiType} format={openapiFormat}')
        case _: raise Exception(f'Unsupported type: "{type}"')

def createOpenApiAnyOf(name,anyOf):
    # logger.debug(f'createOpenApiAnyOf: {anyOf}')
    vars = []
    for item in anyOf:
        vars.append(mapOpenapiType(openapiType=item['type'],openapiFormat=item.get('format')))
    types = [var.type for var in vars]

    if len(vars)==2 and BasicType.null in types:
        var = [item for item in vars if not item.type is BasicType.null]
        if len(var)!=1:
            raise Exception(f'createOpenApiAnyOf: bad types: {vars}')
        var[0].optional=True
        var[0].name = name
        return var[0]
    else:
        raise Exception(f'createOpenApiAnyOf: not supported: {types}')

def register(struct,allObjs):
    if not isinstance(struct,Struct):
        logger.error(f'An attempt to register not a structure! struct={type(struct)}')
        return
    if not struct.name in [obj.name for obj in allObjs]:
        allObjs.append(struct)

def getStructByName(name,allObjs,schemas) -> Struct|None:
    res = [o for o in allObjs if type(o)==Struct and o.name==name]
    match len(res):
        case 0:
            return process_a_thing(name,schemas[name],allObjs,schemas,resolveDependentTypes=True)
        case 1:
            return res[0]
        case _:
            raise Exception(f'internal error, found {len(res)} objects of typeName={name}')

# def read_object_definition(name,obj,allObjs) -> Variable:
#     logger.debug(f'read_object_definition: name={name} {obj}')
#     struct = Struct(name)

#     ctorArgs = []
#     ctorMapping = []

#     for varName, property  in obj.get('properties',{}).items():
#         getType('',property)

#         # logger.debug(f'Adding: {varName} with props: {property}')
#         # required:bool = varName in obj.get('required',[])
#         # if 'type' in property:
#         #     match property['type']:
#         #         case 'array':
#         #             var = createArray(varName,property)
#         #         case _:
#         #             # typeName, typeStruct = getType(property,allObjs)
#         #             var = mapOpenapiType(openapiType=property['type'],openapiFormat=property.get('format'),name=varName)
#         # elif 'anyOf' in property:
#         #     var = createOpenApiAnyOf(varName,property['anyOf'])
#         # else:
#         #     logger.warning(f'Not supported property type: {property}, using "string"')
#         #     var = Variable(name=varName,type=BasicType.string)
#         struct.AddAttribute(copy.deepcopy(var))
#         var.defval = var.CreateDefautValue()
#         ctorArgs.append(var)
#         ctorMapping.append((varName,[Variable(varName)]))

def get_openapi_object_direct_type(obj) -> str:
    '''No recursion!'''
    # logger.debug(f'get_openapi_object_direct_type: {obj}')

    ref   = obj.get('$ref')
    type  = obj.get('type')
    anyOf = obj.get('anyOf')

    # logger.debug(f'get_openapi_object_direct_type: ref={"yes" if ref else "no"} type={"yes" if type else "no"} anyOf={"yes" if anyOf else "no"}')

    if ref:
        assert not type
        assert not anyOf
        return ref.split('/')[-1]
        # raise NotImplementedError

    var = None

    if type:
        assert not anyOf
        return type

    if anyOf:
        return OpenApiType.anyOf

    logger.warning(f'The type is not detected, using "{OpenApiType.string}" by default.')
    return OpenApiType.string

def process_object(name,obj,allObjs,schemas) -> Struct:
    struct = Struct(name)
    register(struct,allObjs)

    ctorArgs = []
    ctorMapping = []

    if not 'properties' in obj:
        logger.warning(f'object "{name}" has no "properties"')

    for varName, property in obj.get('properties',{}).items():
        var = process_a_thing(varName,property,allObjs,schemas,resolveDependentTypes=True)

        if not (type(var)==Variable or type(var)==Struct):
            raise Exception(f'process_a_thing returned type={type(var)} for varName={varName} property={property}')

        required:bool = varName in obj.get('required',[])

        # logger.debug(f'*** object "{name}" property={varName} type={type(var)} required={required}')

        struct.AddAttribute(copy.deepcopy(var))
        if not var.defval:
            var.defval = var.CreateDefautValue()
        ctorArgs.append(var)
        ctorMapping.append((varName,[Variable(varName)]))

    struct.methods.append(Function(
        struct.name,
        'constructor',
        args = ctorArgs,
        mapping = ctorMapping
    ))

    return struct

def process_array(arrayName,obj,allObjs,schemas) -> Variable:
    itemsTypeStr = get_openapi_object_direct_type(obj['items'])
    itemsType = getTypeFromString(itemsTypeStr,allObjs,schemas)
    assert type(itemsType)==Struct or type(itemsType)==Variable
    # logger.debug(f'array itemType={itemsType}')
    return Variable(name=arrayName,type=itemsType,list=True)

def process_anyOf(name,obj,allObjs,schemas) -> Struct|Variable:
    # logger.debug(f'process_anyOf: name="{name}" obj={obj}')
    vars = []
    not_null_vars = []
    for item in obj['anyOf']:
        # logger.debug(f'process_anyOf item: {item}')
        itemTypeStr = get_openapi_object_direct_type(item)
        itemType = getTypeFromString(itemTypeStr,allObjs,schemas)
        # logger.debug(f'anyOf itemType={itemType}')

        if type(itemType)==Struct:
            var = Variable(type=itemType)
        elif type(itemType)==Variable:
            var = itemType
        else:
            raise NotImplementedError
        var.name = f'anyOf{len(vars)}'
        vars.append(var)

        if var.type!=BasicType.null:
            not_null_vars.append(var)

    if len(vars)==2 and len(not_null_vars)==1:
        var = not_null_vars[0]
        var.optional=True
        var.name = name
        return var
    else:
        raise Exception(f'process_anyOf: not supported: {vars}')
    # return Variable(name=name,type=BasicType.string,doc='FIXME: dummy anyOf variable')

def getTypeFromString(typeStr:str,allObjs,schemas) -> Struct|Variable:
    if typeStr in OpenApiBasicType:
        return mapOpenapiType(name='',type=typeStr)
    elif type(typeStr)==str:
        return getStructByName(typeStr,allObjs,schemas)
    else:
        raise Exception(f'NotImplementedError: {typeStr}')

def process_a_thing(objName,obj,allObjs,schemas,resolveDependentTypes=False) -> Struct|Variable:

    objType = get_openapi_object_direct_type(obj)
    
    # logger.debug(f'process_a_thing: name={objName}  type={objType}  isOpenapiType={objType in OpenApiType}')

    if objType in OpenApiDependentType:
        if resolveDependentTypes:
            match objType:
                case OpenApiDependentType.object:
                    a_thing = process_object(objName,obj,allObjs,schemas)
                    assert type(a_thing)==Struct or type(a_thing)==Variable
                    return a_thing
                case OpenApiDependentType.array:
                    a_thing = process_array(objName,obj,allObjs,schemas)
                    assert type(a_thing)==Variable and a_thing.list==True
                    return a_thing
                case OpenApiDependentType.anyOf:
                    a_thing = process_anyOf(objName,obj,allObjs,schemas)
                    assert type(a_thing)==Struct or type(a_thing)==Variable
                    return a_thing
                case _: raise NotImplementedError
        else:
            raise NotImplementedError
    elif objType in OpenApiBasicType:
        var = getTypeFromString(objType,allObjs,schemas)
        assert type(var)==Variable
        var.name = objName
        return var
    elif type(objType)==str:
        struct = getTypeFromString(objType,allObjs,schemas)
        assert type(struct)==Struct
        return struct
    # elif objType in OpenApiBasicType:
    #     return mapOpenapiType(name=objName,type=objType,format=obj.get('format'))
    # elif type(objType)==str:
    #     return getStructByName(objType,allObjs,schemas)
    else:
        raise Exception(f'NotImplementedError: {objType}')

    # logger.debug(f'getType: {obj}')

    # ref   = obj.get('$ref')
    # type  = obj.get('type')
    # anyOf = obj.get('anyOf')

    # # if not ref and not type and not anyOf:
    # #     return defaultType

    # # if ref and type:
    # #     raise Exception('getType: both $ref and type are present!')

    # var = None

    # if type:
    #     logger.debug(f'getType: type="{type}"')
    #     assert not ref
    #     assert not anyOf
    #     # logger.debug(f'ref: {ref}')
    #     # refStructName = ref.split('/')[-1]
    #     # findRef = [o for o in allObjs if type(o)==Struct and o.name==refStructName]
    #     # assert len(findRef)==1
    #     # var = Variable('',type=findRef[0])
    #     if type in OpenApiType:
    #         logger.debug(f'getType: type="{type}" is an OpenApiType')
    #         match type:
    #             case OpenApiType.object:
    #                 read_object_definition(obj,allObjs)
    #             case OpenApiType.array:
    #                 arrayItemType = getType(obj['items'],allObjs)
    #             case _:
    #                 raise Exception(f'Unhandled case: type="{_}')
    #     else:
    #         logger.error(f'getType: type="{type}" is NOT an OpenApiType. findStruct={findStructByName(allObjs,type)}')

    # if ref:
    #     assert not type
    #     assert not anyOf
    #     logger.debug(f'ref: {ref}')
    #     refStructName = ref.split('/')[-1]
    #     findRef = [o for o in allObjs if type(o)==Struct and o.name==refStructName]
    #     assert len(findRef)==1
    #     var = Variable('',type=findRef[0])
    #     # result = (findRef[0].name,findRef[0])
    # # if type:
    # #     if type in OpenApiType:
    # #         return (type,None)

    # logger.debug(f'getType: {obj} => {var}')
    # return var

# def process_openapi_schema_old(name,obj,allObjs,schemas):

#     logger.debug(f'process_openapi_object_schema: name="{name}"  obj: {obj}')
#     logger.debug('getType-A')
#     getType('',obj)

#     struct = Struct(name)

#     ctorArgs = []
#     ctorMapping = []

#     def createArray(arrayName:str,property) -> Variable:
#         # getType(property['items'],allObjs)
#         ref = property['items'].get('$ref')
#         if not ref:
#             logger.warning('$ref not found in property, using "string" as the object type')
#             varType = BasicType.string
#         else:
#             logger.debug(f'ref: {ref}')
#             refStructName = ref.split('/')[-1]
#             findRef = [o for o in allObjs if type(o)==Struct and o.name==refStructName]
#             if len(findRef)==1:
#                 varType = findRef[0]
#                 # assert type2==varType
#             elif len(findRef)==0:
#                 if name!=refStructName:
#                     logger.warning(f'Schema "{name}" is using unknown schema "{refStructName}", resolving...')
#                     varType = process_openapi_schema(refStructName,schemas[refStructName],allObjs,schemas)
#                     register(varType,allObjs)
#                 else:
#                     logger.debug(f'Schema {name} contains an array of itself elements.')
#                     varType = struct
#             else:
#                 raise Exception('openapi specs error?!')
#         return Variable(name=arrayName,type=varType,list=True)

#     if obj.get('type')=='array':
#         var = createArray('items',obj)
#         struct.AddAttribute(copy.deepcopy(var))
#         var.defval = []
#         ctorArgs.append(var)
#         ctorMapping.append((var.name,[Variable(var.name)]))
#     else:
#         assert obj.get('type')=='object'
#         for varName, property  in obj.get('properties',{}).items():
#             logger.debug('getType-C')
#             getType('',property)
#             logger.debug(f'Adding: {varName} with props: {property}')
#             required:bool = varName in obj.get('required',[])
#             if 'type' in property:
#                 match property['type']:
#                     case 'array':
#                         var = createArray(varName,property)
#                     case _:
#                         # typeName, typeStruct = getType(property,allObjs)
#                         var = mapOpenapiType(openapiType=property['type'],openapiFormat=property.get('format'),name=varName)
#             elif 'anyOf' in property:
#                 var = createOpenApiAnyOf(varName,property['anyOf'])
#             else:
#                 logger.warning(f'Not supported property type: {property}, using "string"')
#                 var = Variable(name=varName,type=BasicType.string)
#             struct.AddAttribute(copy.deepcopy(var))
#             var.defval = var.CreateDefautValue()
#             ctorArgs.append(var)
#             ctorMapping.append((varName,[Variable(varName)]))

#     struct.methods.append(Function (
#         struct.name,
#         'constructor',
#         args = ctorArgs,
#         mapping = ctorMapping
#     ))

#     return struct

def schema (openApiConfig:str):

    ext = openApiConfig.split('.')[-1]
    with open(openApiConfig) as file:
        match ext:
            case 'yaml': specs = yaml.safe_load(file)
            case 'json': specs = json.load(file)
            case _: raise Exception(f'Unknown extension {ext}')

    allObjs = []

    schemas = specs['components']['schemas']
    for name, obj in schemas.items():
        process_a_thing(name,obj,allObjs,schemas,resolveDependentTypes=True)
        # register(struct,allObjs)

    return allObjs
