import pytest, logging, os, shutil

from cgdto import Struct, Variable, Function, CodeBlock, supported_languages
from schema_empty import schema as schema_empty
from schema_mcsdk import schema as schema_mcsdk
from schema_openapi import schema as schema_openapi

logger = logging.getLogger(__name__)

@pytest.fixture
def runTests() -> bool:
    return False

@pytest.fixture
def languages():
    return ['python','cpp','typescript']

# @pytest.fixture
# def schemas():
#     return [schema_mcsdk]

@pytest.mark.parametrize("schema", [schema_empty,schema_mcsdk,schema_openapi])
def test_schema(runTests,languages,schema):
    logger.debug(f'languages: {languages}')

    schemaDir = os.path.dirname(schema.__file__)
    logger.debug(f'Schema directory: {schemaDir}')

    objs = schema.schema()

    structs = [o for o in objs if isinstance(o,Struct)]
    funcs   = [o for o in objs if isinstance(o,Function)]
    cblocks = [o for o in objs if isinstance(o,CodeBlock)]
    logger.debug(f'The schema has {len(objs)} objects:  {len(structs)} structs, {len(funcs)} functions and {len(cblocks)} code blocks')

    outdir = f'{schemaDir}/output'
    if os.path.exists(outdir):
        logger.warning(f'Removing the old output: {outdir}')
        shutil.rmtree(outdir)

    options = {
        'outdir':outdir,
        'schema_version':schema.schema_version(),
        'schema_includes_dir':schemaDir
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
