import yaml, logging
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
        # varType:str = self.Type(property['type'],property.get('format',''))
        # if not required:
        #     varType = f'std::optional<{varType}>'
        # self.AppendCode(fileName,line)
        # self.AppendCode(fileName,f'  {varType} {varName};')

    struct.methods.append(Function (
        struct.name,
        'constructor',
        args = ctorArgs,
        mapping = ctorMapping
        # args = [
        #     Variable('name','string',''),
        #     Variable('title','string',''),
        #     Variable('doc_md','string',''),
        #     Variable('start','string',''),
        #     Variable('nargs_min','int',-88),
        #     Variable('nrefs_min','int',-88)
        # ],
        # mapping = [
        #     ('name',[Variable('name')]),
        #     ('title',[Variable('title')]),
        #     ('doc_md',[Variable('doc_md')]),
        #     ('start',[Variable('start')]),
        #     ('nargs_min',[Variable('nargs_min')]),
        #     ('nrefs_min',[Variable('nrefs_min')]),
        # ]
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

def schema (openApiYaml:str):

    specs = yaml.safe_load(open(openApiYaml))

    objs = []

    for name, obj in specs['components']['schemas'].items():
        struct = process_openapi_schema(name,obj)
        if struct:
            objs.append(struct)

    return objs
