import pytest, logging, os, shutil

from cgdto import Struct, Variable, Function, CodeBlock, supported_languages
from empty_schema import schema as empty_schema
from mcsdk_schema import schema as mcsdk_schema
from openapi_schema import schema as openapi_schema

logger = logging.getLogger(__name__)

@pytest.fixture
def runTests() -> bool:
    return True

class Schema:
    def __init__(self,module):
        self.module = module
    def Version(self):
        return self.module.schema_version()
    def Objs(self):
        raise NotImplementedError
    def Dir(self):
        return os.path.dirname(self.module.__file__)
    def OutDir(self):
        return f'{self.Dir()}/output'

class PythonSchema(Schema):
    def __init__(self,module):
        super().__init__(module)
    def Objs(self):
        return self.module.schema()

class OpenapiSchema(Schema):
    def __init__(self,module,configYaml:str):
        super().__init__(module)
        self.configYaml = configYaml
    def Objs(self):
        return self.module.schema(os.path.join(self.Dir(),self.configYaml))
    def OutDir(self):
        return f'{self.Dir()}/{os.path.splitext(self.configYaml)[0]}_output'

@pytest.mark.parametrize(
        "schema, languages",
        [
            (PythonSchema(empty_schema), ['python','cpp','typescript']),
            (PythonSchema(mcsdk_schema), ['python','cpp','typescript']),
            (OpenapiSchema(openapi_schema,'petstore.yaml'), ['python','cpp','typescript']),
            (OpenapiSchema(openapi_schema,'property_anyOf.yaml'), ['python','cpp','typescript']),
            (OpenapiSchema(openapi_schema,'array_and_boolean.yaml'), ['python','cpp','typescript']),
        ]
)

def test_schema(runTests,languages,schema):
    logger.debug(f'languages: {languages}')

    logger.debug(f'Schema directory: {schema.Dir()}')

    objs = schema.Objs()

    structs = [o for o in objs if isinstance(o,Struct)]
    funcs   = [o for o in objs if isinstance(o,Function)]
    cblocks = [o for o in objs if isinstance(o,CodeBlock)]
    logger.debug(f'The schema has {len(objs)} objects:  {len(structs)} structs, {len(funcs)} functions and {len(cblocks)} code blocks')

    outdir = schema.OutDir()
    if os.path.exists(outdir):
        logger.warning(f'Removing the old output: {outdir}')
        shutil.rmtree(outdir)

    options = {
        'outdir':outdir,
        'schema_version':schema.Version(),
        'schema_includes_dir':schema.Dir()
    }

    code = {}
    for lang in languages:
        code[lang] = supported_languages[lang] (options)
        code[lang].Process(objs)

        if runTests:
            code[lang].CreateTestEnv(objs)

    if runTests:
        for lang1 in languages:
            if not code[lang1].test_environment_ready:
                logger.warning(f'Language "{lang1}" has no run test environment')
                continue
            for lang2 in languages:
                if not code[lang1].test_environment_ready:
                    continue
                logger.info(f'Testing: {lang1} with {lang2}')
                code[lang1].RunTests(code[lang2],objs)
