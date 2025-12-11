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
            return process_a_thing(name,schemas[name],allObjs,schemas)
        case 1:
            return res[0]
        case _:
            raise Exception(f'internal error, found {len(res)} objects of typeName={name}')

def get_openapi_object_direct_type(obj) -> str:
    '''No recursion!'''

    ref   = obj.get('$ref')
    type  = obj.get('type')
    anyOf = obj.get('anyOf')

    if ref:
        assert not type
        assert not anyOf
        return ref.split('/')[-1]

    var = None

    if type:
        assert not anyOf
        return type

    if anyOf:
        return OpenApiType.anyOf

    logger.warning(f'The type is not detected, using "{OpenApiType.string}" by default: {obj}')
    return OpenApiType.string

def process_object(name,obj,allObjs,schemas) -> Struct:
    struct = Struct(name)
    register(struct,allObjs)

    ctorArgs = []
    ctorMapping = []

    if not 'properties' in obj:
        logger.warning(f'object "{name}" has no "properties"')

    for varName, property in obj.get('properties',{}).items():
        var = process_a_thing(varName,property,allObjs,schemas)

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
    array = process_a_thing(arrayName,obj['items'],allObjs,schemas)
    logger.debug(f'process_array: {array}')
    assert type(array)==Variable
    assert not array.list
    array.list = True
    return array

def newStructName(pattern:str,allObjs,maxStructs=100):
    for i in range(maxStructs):
        name = f'{pattern}{i}'
        if not [o for o in allObjs if type(o)==Struct and o.name==name]:
            return name
    raise Exception(f'Failed to generate a newStructName with pattern={pattern} maxStructs={maxStructs}')

def process_anyOf(name,obj,allObjs,schemas) -> Struct|Variable:
    vars = []
    not_null_vars = []
    for item in obj['anyOf']:
        itemTypeStr = get_openapi_object_direct_type(item)
        itemType = getTypeFromString(itemTypeStr,allObjs,schemas)

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
        var.optional = True
        var.name = name
        return var

    match len(vars):
        case 0:
            raise Exception(f'anyOf without any items')
        case 1:
            return vars[0]
        case _:
            struct = Struct(newStructName('AnyOf',allObjs))
            register(struct,allObjs)
            
            ctorArgs = []
            ctorMapping = []

            for var in vars:
                if type(var.type)==Struct:
                    struct.AddDependency(var.type)
                var.optional = True
                struct.AddAttribute(copy.deepcopy(var))
                if not var.defval:
                    var.defval = var.CreateDefautValue()
                ctorArgs.append(var)
                ctorMapping.append((var.name,[Variable(var.name)]))

            struct.methods.append(Function(
                struct.name,
                'constructor',
                args = ctorArgs,
                mapping = ctorMapping
            ))

            return Variable(name,type=struct)

    raise Exception(f'process_anyOf: not supported: {vars}')

def getTypeFromString(typeStr:str,allObjs,schemas) -> Variable:
    if typeStr in OpenApiBasicType:
        return mapOpenapiType(name='',type=typeStr)
    elif type(typeStr)==str:
        struct = getStructByName(typeStr,allObjs,schemas)
        assert type(struct)==Struct
        return Variable(name='',type=struct)
    else:
        raise Exception(f'NotImplementedError: {typeStr}')

def process_a_thing(objName,obj,allObjs,schemas) -> Struct|Variable:

    objType = get_openapi_object_direct_type(obj)
    
    logger.debug(f'process_a_thing: name={objName}  type={objType}  isOpenapiType={objType in OpenApiType}')

    if objType in OpenApiDependentType:
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
    elif objType in OpenApiBasicType or type(objType)==str:
        var = getTypeFromString(objType,allObjs,schemas)
        logger.debug(f'from getTypeFromString: {var}')
        assert type(var)==Variable
        var.name = objName
        return var
    else:
        raise Exception(f'NotImplementedError: {objType}')

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
        process_a_thing(name,obj,allObjs,schemas)

    return allObjs
