import json, yaml, logging, copy
from enum import StrEnum, auto

from cgdto import *

logger = logging.getLogger(__name__)

def schema_version () -> str:
    return 'OpenApi schema (0.1.0)'

class OpenApi:
    class Type(StrEnum):
        null    = auto()
        boolean = auto()
        array   = auto()
        object  = auto()
        number  = auto()
        integer = auto()
        string  = auto()
    class Format(StrEnum):
        none  = ''
        int32 = auto()
        int64 = auto()

def mapOpenapiType(openapiType:str,openapiFormat:str='',name='') -> Variable:
    if openapiFormat:
        logger.warning(f'openapiFormat="{openapiFormat}" is ignored')
    match openapiType:
        case OpenApi.Type.null:
            return Variable(name=name,type=BasicType.null)
        case OpenApi.Type.boolean:
            return Variable(name=name,type=BasicType.boolean)
        case OpenApi.Type.number:
            return Variable(name=name,type=BasicType.float)
        case OpenApi.Type.integer:
            return Variable(name=name,type=BasicType.int)
            # match openapiFormat:
            #     case OpenApi.Format.none: return 'int'
            #     case OpenApi.Format.int32: return 'int'
            #     case OpenApi.Format.int64: return 'int'
            #     case _: raise Exception(f'{self.langName} unsupported type={openapiType} format={openapiFormat}')
        case OpenApi.Type.string:
            return Variable(name=name,type=BasicType.string)
        case OpenApi.Type.array:
            return Variable(name=name,type=BasicType.null,list=True)
            # return BasicType.string
            # match openapiFormat:
            #     case '': return 'std::string'
            #     case _: raise Exception(f'{self.langName} unsupported type={openapiType} format={openapiFormat}')
        case _: raise Exception(f'Unsupported type: "{openapiType}"')

def createOpenApiAnyOf(name,anyOf):
    logger.debug(f'createOpenApiAnyOf: {anyOf}')
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

def process_openapi_schema(name,obj,allObjs):

    logger.debug(f'process_openapi_object_schema: {name}')

    struct = Struct(name)

    ctorArgs = []
    ctorMapping = []

    def createArray(name:str,property) -> Variable:
        ref = property['items']['$ref']
        logger.debug(f'ref: {ref}')
        refStructName = ref.split('/')[-1]
        findRef = [o for o in allObjs if type(o)==Struct and o.name==refStructName]
        if len(findRef)!=1:
            raise Exception(f'found {len(findRef)} objects "{refStructName}"')
        return Variable(name=name,type=findRef[0],list=True)

    if obj.get('type')=='array':
        var = createArray('items',obj)
        struct.AddAttribute(copy.deepcopy(var))
        var.defval = []
        ctorArgs.append(var)
        ctorMapping.append((var.name,[Variable(var.name)]))
    else:
        for varName, property  in obj.get('properties',{}).items():
            logger.debug(f'Adding: {varName} with props: {property}')
            required:bool = varName in obj.get('required',[])
            if 'type' in property:
                match property['type']:
                    case 'array':
                        var = createArray(varName,property)
                    case _:
                        var = mapOpenapiType(openapiType=property['type'],openapiFormat=property.get('format'),name=varName)
            elif 'anyOf' in property:
                var = createOpenApiAnyOf(varName,property['anyOf'])
            else:
                raise Exception(f'Not supported property type: {property}')
            struct.AddAttribute(copy.deepcopy(var))
            var.defval = var.CreateDefautValue()
            ctorArgs.append(var)
            ctorMapping.append((varName,[Variable(varName)]))

    struct.methods.append(Function (
        struct.name,
        'constructor',
        args = ctorArgs,
        mapping = ctorMapping
    ))

    return struct

# def process_openapi_array_schema(name,obj,allObjs):
    

# def process_openapi_schema(name,obj,allObjs):
#     match obj['type']:
#         case OpenApi.Type.object: return process_openapi_object_schema(name,obj,allObjs)
#         case OpenApi.Type.array:  return process_openapi_array_schema (name,obj,allObjs)
#         case _: raise Exception(f'Not supported schema type: {obj["type"]}')

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
