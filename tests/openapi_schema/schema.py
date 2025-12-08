import json, yaml, logging
from enum import StrEnum, auto

from cgdto import *

logger = logging.getLogger(__name__)

def schema_version () -> str:
    return 'OpenApi schema (0.1.0)'

class OpenApi:
    class Type(StrEnum):
        null    = auto()
        # boolean = 'boolean'
        array   = auto()
        object  = auto()
        number  = auto()
        integer = auto()
        string  = auto()
    class Format(StrEnum):
        none  = ''
        int32 = auto()
        int64 = auto()

def mapOpenapiType(openapiType:str,openapiFormat:str) -> BasicType:
    match openapiType:
        case OpenApi.Type.null:
            return BasicType.null
        case OpenApi.Type.number:
            return BasicType.float
        case OpenApi.Type.integer:
            return BasicType.int
            # match openapiFormat:
            #     case OpenApi.Format.none: return 'int'
            #     case OpenApi.Format.int32: return 'int'
            #     case OpenApi.Format.int64: return 'int'
            #     case _: raise Exception(f'{self.langName} unsupported type={openapiType} format={openapiFormat}')
        case OpenApi.Type.string:
            return BasicType.string
            # match openapiFormat:
            #     case '': return 'std::string'
            #     case _: raise Exception(f'{self.langName} unsupported type={openapiType} format={openapiFormat}')
        case _: raise Exception(f'Unsupported type: "{openapiType}"')

def createOpenApiAnyOf(name,anyOf):
    logger.debug(f'createOpenApiAnyOf: {anyOf}')
    types = []
    for item in anyOf:
        types.append(mapOpenapiType(item['type'],item.get('format')))

    logger.debug(f'createOpenApiAnyOf: types: {types}')

    if len(types)==2 and BasicType.null in types:
        logger.debug('Converting into optional!')
            # Variable('RandomSeed','int',None,optional=True),
        qtype = [item for item in types if not item is BasicType.null]
        if len(qtype)!=1:
            raise Exception(f'createOpenApiAnyOf: bad types: {types}')
        return Variable(name=name,type=qtype[0],optional=True)
    else:
        raise Exception(f'createOpenApiAnyOf: not supported: {types}')
    
    raise NotImplementedError

def process_openapi_object_schema(name,obj,allObjs):

    logger.debug(f'process_openapi_object_schema: {name}')

    struct = Struct(name)

    ctorArgs = []
    ctorMapping = []

    for varName,property  in obj.get('properties',{}).items():
        required:bool = varName in obj.get('required',[])
        if 'type' in property:
            var = Variable(name=varName,type=mapOpenapiType(property['type'],property.get('format')))
        elif 'anyOf' in property:
            var = createOpenApiAnyOf(varName,property['anyOf'])
        else:
            raise Exception(f'Not supported property type: {property}')
        struct.AddAttribute(var)
        var.defval = None if var.optional else typeDefaultValue(var.type)
        ctorArgs.append(var)
        ctorMapping.append((varName,[Variable(varName)]))

    # variant = []
    # for item in obj.get('oneOf',[])+obj.get('anyOf',[]):
    #     logger.debug(f'oneOf+anyOf: {item}')

    #     processed = False

    #     ref = item.get('$ref',None)
    #     logger.debug(f'ref: {ref}')
    #     if ref:
    #         refStructName = ref.split('/')[-1]
    #         findRef = [o for o in allObjs if type(o)==Struct and o.name==refStructName]
    #         if len(findRef)!=1:
    #             raise Exception(f'found {len(findRef)} objects "{refStructName}"')
    #         struct.AddDependency(findRef[0])
    #         variant.append(findRef[0])
    #         processed = True
        
    #     ptype = item.get('type',None)
    #     logger.debug(f'type: {ptype}')
    #     if ptype:
    #         # refStructName = ref.split('/')[-1]
    #         # findRef = [o for o in allObjs if type(o)==Struct and o.name==refStructName]
    #         # if len(findRef)!=1:
    #         #     raise Exception(f'found {len(findRef)} objects "{refStructName}"')
    #         # struct.AddDependency(findRef[0])
    #         variant.append(ptype)
    #         processed = True

    #     if not processed:
    #         raise Exception(f'oneOf+anyOf: not supported: {item}')
    # if variant:
    #     varType = 'variant'
    #     varName = 'oneOfanyOf'
    #     struct.AddAttribute(Variable(name=varName,type=varType,variant=variant))
    #     firstVariant = variant[0]
    #     if isinstance(firstVariant,Struct):
    #         ctorArgs.append(Variable(name=varName,type=varType,variant=variant,defval=Variable(f'{firstVariant.name}()',firstVariant)))
    #     # elif firstVariant==OpenApi.Type.null:
    #     #     ctorArgs.append(Variable(name=varName,type=varType,variant=variant,defval=Variable(f'{firstVariant.name}()',firstVariant)))
    #     else:
    #         raise Exception(f'Not supported: {firstVariant} of type {type(firstVariant)}')
    #     ctorMapping.append((varName,[Variable(varName)]))

    struct.methods.append(Function (
        struct.name,
        'constructor',
        args = ctorArgs,
        mapping = ctorMapping
    ))

    return struct

def process_openapi_array_schema(name,obj,allObjs):
    logger.error('process_openapi_array_schema: no code!!!')
    return None

def process_openapi_schema(name,obj,allObjs):
    match obj['type']:
        case OpenApi.Type.object: return process_openapi_object_schema(name,obj,allObjs)
        case OpenApi.Type.array:  return process_openapi_array_schema (name,obj,allObjs)
        case _: raise Exception(f'Not supported schema type: {obj["type"]}')

def schema (openApiConfig:str):

    ext = openApiConfig.split('.')[-1]
    with open(openApiConfig) as file:
        match ext:
            case 'yaml': specs = yaml.safe_load(file)
            case 'json': specs = json.load(file)
            case _: raise Exception(f'Unknown extension {ext}')

    allObjs = []

    for name, obj in specs['components']['schemas'].items():
        struct = process_openapi_schema(name,obj,allObjs)
        if struct:
            allObjs.append(struct)

    return allObjs
