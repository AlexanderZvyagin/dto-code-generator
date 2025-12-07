import pytest, logging, os, shutil

from cgdto import Struct, Variable, Function, CodeBlock, supported_languages
import schema

logger = logging.getLogger(__name__)

@pytest.fixture
def languages():
    return ['python','cpp','typescript']

def test_mcsdk(languages):
    logger.debug(f'languages: {languages}')

    schemaDir = os.path.dirname(schema.__file__)
    logger.debug(f'Schema directory: {schemaDir}')

    objs = schema.schema()

    structs = [o for o in objs if isinstance(o,Struct)]
    funcs   = [o for o in objs if isinstance(o,Function)]
    cblocks = [o for o in objs if isinstance(o,CodeBlock)]
    logger.debug(f'The schema has {len(objs)} objects:  {len(structs)} structs, {len(funcs)} functions and {len(cblocks)} code blocks')

    outdir = f'{schemaDir}/output'
    if os.path.exists:
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

        code[lang].CreateTestEnv(objs)

    for lang1 in languages:
        if not code[lang1].test_environment_ready:
            logger.warning(f'Language "{lang1}" has no run test environment')
            continue
        for lang2 in languages:
            if not code[lang1].test_environment_ready:
                continue
            logger.info(f'Testing: {lang1} with {lang2}')
            code[lang1].RunTests(code[lang2],objs)
