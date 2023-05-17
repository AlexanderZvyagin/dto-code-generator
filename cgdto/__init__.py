from .all import *
from .python import *
from .typescript import *
from .cpp import *
from .csharp import *
from .Code_Python import *
from .Code_Cpp import *
from .Code_Typescript import *

def write_objs (
    dir_dto     : str,
    dir_tests   : str,
    language    : str,
    objs        : any        = [],
    schema      : str = ''
):
    '''fname: full path name without extension, the file will be overwritten. the directory path must exist.'''

    file_writer = globals().get(f'FileWriter_{language}')
    if file_writer:
        return file_writer(dir_dto,dir_tests,objs,schema)

    with open(f'{dir_dto}/dto.{ext[language]}','w') as file:
        file_prefix_code = globals().get(f'File_prefix_{language}')
        if file_prefix_code:
            for line in file_prefix_code(objs,schema):
                file.write(line+'\n')
        for obj in objs:
            if isinstance(obj,Struct):
                name = f'Struct_{language}'
                func = globals().get(name)
                if func:
                    for line in func(obj):
                        file.write(line+'\n')
                    file.write('\n')
                else:
                    print(f'There is no function {name}')
            elif isinstance(obj,CodeBlock):
                for line in obj.code.get(language,[]):
                    file.write(line+'\n')
            elif isinstance(obj,Function):
                name = f'Function_{language}'
                func = globals().get(name)
                if func:
                    for line in func(obj):
                        file.write(line+'\n')
            else:
                print(f'Cannot handle {type(obj)}')

        file_suffix_code = globals().get(f'File_suffix_{language}')
        if file_suffix_code:
            for line in file_suffix_code(objs):
                file.write(line+'\n')

    if 1:
        name = f'Tests_{language}'
        func = globals().get(name)
        if not func:
            print(f'No code for {name}')
        else:
            with open(f'{dir_tests}/{name_dto_tests}.{ext[language]}','w') as file:
                for line in func(objs):
                    file.write(line+'\n')
