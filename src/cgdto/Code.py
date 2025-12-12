import os, logging
from .all import *

logger = logging.getLogger(__name__)

'''
The generator interface does not know:
- how many files will be generated
- what are the file names, the purpose of files

yield {'directory':outdir,'file':file_name,'line':code_line}
yield {'path':relative_path,'line':code_line}


Split the functionality of CodeGeneratorOfMyLanguage:
- there are language specific settings, like:
    - set of functions to use
    - single/multiple DTOs to generate
    - detecting run time environment
- lnguage-independent steps:
    - generate DTO code (directories and files)
    - generate tests (directories and files)
    - generate language specific run test environment (directories and files PLUS language specific tools using shell-subprocess)
    - allow to run tests ()
'''

class Code:
    def __init__ (self, language, extension, options={}):
        self.language       = language
        self.extension      = extension
        self.options        = options
        self.name_dto       = 'dto'
        self.name_test      = 'test'
        self.name_test_env  = 'test_rundir'
        self.outdir         = 'outdir'
        self.test_environment_ready = False

    def Process (self, objs):

        os.makedirs (self.GetDirDto(), exist_ok=True)

        files = {}
        for path,line in self.GeneratorFiles (objs):
            if not path in files:
                head, tail = os.path.split (path)
                logger.info(f'creating file "{path}"')
                if head:
                    os.makedirs (head, exist_ok=True)
                file = open(path,'w')
                files[path] = file
            else:
                file = files[path]
            file.write(line+'\n')

        for path,file in files.items():
            file.close()

    def GeneratorFiles (self, objs):
        for item in self.GeneratorDto (objs):
            yield item
        for item in self.GeneratorTests (objs):
            yield item

    def GetDirDto (self):
        return f'{self.options[self.outdir]}/{self.name_dto}/{self.language}'

    def GetDirTest (self):
        return f'{self.options[self.outdir]}/{self.name_test}/{self.language}'

    def GetDirTestEnv (self):
        return f'{self.options[self.outdir]}/{self.name_test_env}/{self.language}'

    def RunTests (self, other, objs):

        for obj in objs:
            if not isinstance(obj,Struct):
                continue
            if not (obj.gen_test and obj.default_version):
                continue
            logger.info(f'  Testing [{self.language}] {obj.name}')
            struct_name = obj.name
            outdir1 = self.GetDirTestEnv()
            outdir2 = self.GetDirTestEnv()

            lang1 = self.language
            lang2 = other.language

            json_file1 = f'{outdir1}/{struct_name}-created-by-{lang1}.json'
            run_test(f'{outdir1}','create',struct_name,json_file1)
            json_file2 = f'{outdir1}/{struct_name}-created-by-{lang1}-converted-by-{lang2}.json'
            run_test(f'{outdir2}','convert',struct_name,json_file1,json_file2)
            run_test(f'{outdir1}','compare',struct_name,json_file1,json_file2)

    # The following methods need to be implemented be derived class

    def GeneratorDto (self, objs):
        logger.warning(f'GeneratorDto is not implemented for {self.language}')
        return ()

    def GeneratorTests (self, objs):
        logger.warning(f'GeneratorTests is not implemented for {self.language}')
        return ()

    def CreateTestEnv (self, objs):
        logger.warning(f'CreateTestEnv is not implemented for {self.language}')
        return ()
