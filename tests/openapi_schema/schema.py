import json, yaml, logging
from enum import StrEnum

from cgdto import *

logger = logging.getLogger(__name__)

def schema_version () -> str:
    return 'OpenApi schema (0.1.0)'

class OpenApi:
    class Type(StrEnum):
        integer = 'integer'
        string = 'string'
    class Format(StrEnum):
        none  = ''
        int32 = 'int32'
        int64 = 'int64'

def mapOpenapiType(openapiType:str,openapiFormat:str) -> str:
    match openapiType:
        case OpenApi.Type.integer:
            return 'int'
            # match openapiFormat:
            #     case OpenApi.Format.none: return 'int'
            #     case OpenApi.Format.int32: return 'int'
            #     case OpenApi.Format.int64: return 'int'
            #     case _: raise Exception(f'{self.langName} unsupported type={openapiType} format={openapiFormat}')
        case OpenApi.Type.string:
            return 'string'
            # match openapiFormat:
            #     case '': return 'std::string'
            #     case _: raise Exception(f'{self.langName} unsupported type={openapiType} format={openapiFormat}')
        case _: raise Exception(f'Unsupported type: {openapiType}')

def process_openapi_object_schema(name,obj):

    struct = Struct(name)

    ctorArgs = []
    ctorMapping = []

    logger.debug(name)
    for varName,property  in obj['properties'].items():
        required:bool = varName in obj.get('required',[])
        line:str = f'  // {varName}  type={property["type"]}  format={property.get("format")} required={required}'
        logger.debug(line)
        varType = mapOpenapiType(property['type'],property.get('format'))
        struct.AddAttribute(Variable(varName,varType))
        ctorArgs.append(Variable(name=varName,type=varType,defval=typeDefaultValue(varType)))
        ctorMapping.append((varName,[Variable(varName)]))

    struct.methods.append(Function (
        struct.name,
        'constructor',
        args = ctorArgs,
        mapping = ctorMapping
    ))

    return struct

def process_openapi_array_schema(name,obj):
    logger.error('process_openapi_array_schema: no code!!!')
    return None

def process_openapi_schema(name,obj):
    match obj['type']:
        case 'object': return process_openapi_object_schema(name,obj)
        case 'array':  return process_openapi_array_schema(name,obj)
        case _: raise Exception(f'Not supported schema type: {obj["type"]}')

def schema (openApiConfig:str):

    ext = openApiConfig.split('.')[-1]
    with open(openApiConfig) as file:
        match ext:
            case 'yaml': specs = yaml.safe_load(file)
            case 'json': specs = json.load(file)
            case _: raise Exception(f'Unknown extension {ext}')

    objs = []

    for name, obj in specs['components']['schemas'].items():
        struct = process_openapi_schema(name,obj)
        if struct:
            objs.append(struct)

    return objs
