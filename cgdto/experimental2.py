import os
from .all import *

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

    def Process (self, objs, args):

        files = {}
        for path,line in self.GeneratorFiles (objs, args):
            if not path in files:
                head, tail = os.path.split (path)
                print(f'creating file "{path}"')
                if head:
                    os.makedirs (head, exist_ok=True)
                file = open(path,'w')
                files[path] = file
            else:
                file = files[path]
            file.write(line+'\n')

        for path,file in files.items():
            file.close()

        self.CreateTestEnv (objs, args)

    def GeneratorFiles (self, objs, args):
        for item in self.GeneratorDto (objs, args):
            yield item
        for item in self.GeneratorTests (objs, args):
            yield item

    def GeneratorDto (self, objs, args):
        print(f'GeneratorDto is not implemented for {self.language}')
        return ()

    def GeneratorTests (self, objs, args):
        print(f'GeneratorTests is not implemented for {self.language}')
        return ()

    def CreateTestEnv (self, objs, args):
        print(f'CreateTestEnv is not implemented for {self.language}')
        return ()

    def GetDirDto (self, args):
        return f'{args["outdir"]}/{self.name_dto}/{self.language}'

    def GetDirTest (self, args):
        return f'{args["outdir"]}/{self.name_test}/{self.language}'

    def GetDirTestEnv (self, args):
        return f'{args["outdir"]}/{self.name_test_env}/{self.language}'

class CodePython (Code):
    def __init__ (self):
        super().__init__('python','py')

    def TypeToString (self, var:Variable) -> str:

        m = {
            'void'    : 'void',
            'string'  : 'str',
            'boolean' : 'bool',
            'int'     : 'int',
            'float'   : 'float',
        }

        tname = var.TypeName()

        kv = detect_dict_key_value(tname)
        if kv:
            tname = f'dict[{m.get(kv[0],kv[0])},{m.get(kv[1],kv[1])}]'

        type_str = m.get(tname,tname)

        if var.list:
            type_str = f'list[{type_str}]'
        if var.optional:
            type_str = f'{type_str}|None'
        return type_str

    def ValueToString (self, arg) -> str:
        if isinstance(arg,Variable):
            return arg.name
        elif isinstance(arg,list):
            x = [ f'{item.name}'   for item in arg]
            y = ','.join(x)
            return f'[{y}]'
        elif isinstance(arg,str):
            return f'"{arg}"'
        else:
            return str(arg)

    def GeneratorDto (self, objs, args):
        path = f'{self.GetDirDto(args)}/{self.name_dto}.{self.extension}'

        for line in self.GeneratorSingleDtoFilePrefix (objs, args):
            yield (path, line)

        for line in self.GeneratorSingleDtoFileBody   (objs, args):
            yield (path, line)

        for line in self.GeneratorSingleDtoFileSuffix (objs, args):
            yield (path, line)

    def GeneratorTests (self, objs, args):
        path = f'{self.GetDirTest(args)}/{self.name_test}.{self.extension}'

        for line in self.GeneratorTest (objs, args):
            yield (path, line)

    def GeneratorSingleDtoFilePrefix (self, objs, args):
        schema_version = args.get('schema_version')
        if schema_version:
            for line in autogen_text(schema_version).split('\n'):
                yield f'# {line}'

        code = f'''
from copy import deepcopy
import math
from math import nan
import json
try:
    import pandas as pd
except:
    print('Warning: "pandas" package was not found.')

def float_equal(a:float|None, b:float|None) -> bool:
    if a is None and b is None: return True
    if a is None and b is not None: return False
    if b is None and a is not None: return False
    if math.isnan(a) and math.isnan(b): return True
    eps = 1e-9
    ab_diff = abs(a-b)
    if ab_diff<eps: return True
    ab_ratio = ab_diff/(abs(a/2 + b/2) + eps)
    if ab_ratio<eps: return True
    return False

'''
        for line in code.split('\n'):
            yield line

    def GeneratorSingleDtoFileSuffix (self, objs, args):
        return ()

    def GeneratorSingleDtoFileBody (self, objs, args):
        for obj in objs:
            if isinstance(obj,Struct):
                for line in self.GeneratorStruct(obj):
                    yield line
                yield ''
            elif isinstance(obj,Function):
                for line in self.GeneratorFunction(objs):
                    yield line
                yield ''
            elif isinstance(obj,CodeBlock):
                for line in obj.code.get(self.language,[]):
                    yield line
                yield ''
            else:
                print(f'Cannot handle {type(obj)}')

    def GeneratorStruct (self, obj:Struct):

        yield f'# Forward declaration'
        yield f'class {obj.name}: pass'

        if obj.base:
            yield f'class {obj.name} ({obj.base.name}):'
        else:
            yield f'class {obj.name}:'
        yield ''

        for attr in obj.attributes:
            if attr.static:
                assert attr.defval is not None
                yield f'{indent}{attr.name} : {self.TypeToString(attr)} = {self.ValueToString(attr.defval)}'

        for func in obj.methods:
            if func.code and func.code.get('python','') is None: continue
            for line in self.GeneratorFunction(func,obj):
                yield f'{indent}{line}'
            yield ''

        yield f'{indent*1}def __eq__ (self, other):'
        if obj.base:
            yield f'{indent*2}if not super().__eq__(other): return False'
        for attr in obj.attributes:
            if attr.skip_dto: continue
            # # FIXME: handle float comparisons
            # if attr.TypeName()=='float' and not attr.list:
            #     yield f'{indent*2}if not float_equal(self.{attr.name},other.{attr.name}): return False'
            # else:
            #     yield f'{indent*2}if self.{attr.name} != other.{attr.name}: return False'
            yield f'{indent*2}if self.{attr.name} != other.{attr.name}: return False'
        yield f'{indent*2}return True'

        yield f'{indent*1}def __neq__ (self, other):'
        yield f'{indent*2}return not self==other'

        yield f'{indent*1}def json (self) -> str:'
        yield f'{indent*2}return {obj.name}_to_json_string(self)'

        for line in self.GeneratorStructFromJsonString(obj):
            yield line
        for line in self.GeneratorStructToJsonString(obj):
            yield line
        # code.extend(Struct_from_json_string_python(self))
        # code.extend(Struct_to_json_string_python(self))

        for line in self.GeneratorStructFromJson(obj):
            yield line
        for line in self.GeneratorStructToJson(obj):
            yield line
        # code.extend(Struct_from_json_python(self))
        # code.extend(Struct_to_json_python(self))

    def GeneratorFunction (self, func:Function, base:Struct=None) -> list[str]:
        if base and func.name==base.name:
            for line in self.GeneratorConstructor(func,base):
                yield line
        else:
            yield f'def {func.name} ('
            if base:
                yield f'{indent}self,'

            for i,a in enumerate(func.args):
                default = '' if a.defval is None else f' = {self.ValueToString(a.defval)}'
                yield f'{indent}{a.name}{default},'
            yield '):'

        for line in get_code(func.code.get('python')):
            yield f'{indent}{line}'

        yield f'{indent}pass'

    def GeneratorConstructor(self, ctor:Function, base:Struct=None):
        assert ctor.name == base.name

        yield ''
        
        yield f'def __init__ ('
        yield f'{indent}self,'
        for i,arg in enumerate(ctor.args):
            defval = ''
            if arg.defval is not None:
                defval = f' = {self.ValueToString(arg.defval)}'
            elif arg.optional:
                defval = ' = None'
            else:
                defval = ''
            yield f'{indent}{arg.name}:{self.TypeToString(arg)}{defval}{"," if i+1<len(ctor.args) else ""}'
        yield f'):'

        for i,(name,mapping) in enumerate(ctor.mapping):
            if base.base and name==base.base.name:
                yield f'{indent}super().__init__('
                for arg in mapping:
                    yield f'{indent*2}{self.ValueToString(arg)},'
                yield f'{indent})'
            else:
                assert len(mapping)==1
                arg = mapping[0]

                attr = None
                for a in base.attributes:
                    if a.static: continue
                    if a.name == name:
                        attr = a
                assert attr is not None
                if isinstance(attr.type,Struct) and isinstance(arg,Variable):
                    yield f'{indent*1}self.{attr.name} : {self.TypeToString(attr)} = deepcopy({self.ValueToString(arg)})'
                else:
                    yield f'{indent*1}self.{attr.name} : {self.TypeToString(attr)} = {self.ValueToString(arg)}'

    def GeneratorStructFromJson (self, obj:Struct):
        yield f'def {obj.name}_from_json (j:dict, obj:{obj.name}):'
        yield f'{indent}assert isinstance(obj,{obj.name})'
        if obj.base:
            yield f'{indent}{obj.base.name}_from_json(j,obj)'

        for attr in obj.attributes:
            if attr.skip_dto: continue

            n = 1
            if attr.optional:
                yield f'{indent*1}if j.get("{attr.name}",None) is not None:'
                n += 1
            if isinstance(attr.type,Struct):
                if attr.list:
                    yield f'{indent*(n+0)}obj.{attr.name} = []'
                    yield f'{indent*(n+0)}for item in j["{attr.name}"]:'
                    yield f'{indent*(n+1)}v = {attr.TypeName()}()'
                    yield f'{indent*(n+1)}{attr.TypeName()}_from_json(item,v)'
                    yield f'{indent*(n+1)}obj.{attr.name}.append(v)'
                else:
                    if attr.optional:
                        yield f'{indent*(n+0)}obj.{attr.name} = {attr.TypeName()}()'
                    yield f'{indent*(n+0)}{attr.TypeName()}_from_json(j["{attr.name}"],obj.{attr.name})'
            else:
                yield f'{indent*(n+0)}obj.{attr.name} = j["{attr.name}"]'

    def GeneratorStructFromJsonString (self, obj:Struct):
        yield f'def {obj.name}_from_json_string (jstr):'
        yield f'{indent}j = json.loads(jstr)'
        yield f'{indent}obj = {obj.name}()'
        yield f'{indent}{obj.name}_from_json(j,obj)'
        yield f'{indent}return obj'
        yield ''

    def GeneratorStructToJson (self, obj:Struct):
        yield f'def {obj.name}_to_json(j:dict, obj:{obj.name}):'
        if obj.base:
            yield f'{indent}{obj.base.name}_to_json(j,obj)'
        for attr in obj.attributes:
            if attr.skip_dto: continue
            var_code = []

            code_not_optional = []

            # Ignore optionality first
            # For a naitive type, we don't need to check the 'list' attribute
            if isinstance(attr.type,str):
                code_not_optional.append(f'j["{attr.name}"] = obj.{attr.name}')
            elif isinstance(attr.type,Struct) and not attr.list:
                code_not_optional.append(f'jj = {{}}')
                code_not_optional.append(f'{attr.TypeName()}_to_json(jj,obj.{attr.name})')
                code_not_optional.append(f'j["{attr.name}"] = jj')
            elif isinstance(attr.type,Struct) and attr.list:
                code_not_optional.append(f'j["{attr.name}"] = []')
                code_not_optional.append(f'for item in obj.{attr.name}:')
                code_not_optional.append(f'{indent}jj = {{}}')
                code_not_optional.append(f'{indent}{attr.TypeName()}_to_json(jj,item)')
                code_not_optional.append(f'{indent}j["{attr.name}"].append(jj)')
            else:
                raise NotImplementedError()

            if attr.optional:
                yield f'{indent}if obj.{attr.name} is not None:'
                n = 2
            else:
                n = 1
            for line in code_not_optional:
                yield f'{indent*n}{line}'
        yield f'{indent}pass'

    def GeneratorStructToJsonString (self, obj:Struct):
        yield f'def {obj.name}_to_json_string (self:{obj.name}):'
        yield f'{indent}j = {{}}'
        yield f'{indent}{obj.name}_to_json(j,self)'
        yield f'{indent}return json.dumps(j)'

    def GeneratorTest (self, objs, args):

        struct_names = []
        code_construct_random = []
        code_create = []
        code_convert = []
        code_compare = []

        for obj in objs:
            if not isinstance(obj,Struct):
                continue
            if not obj.gen_test:
                continue

            struct_names.append(obj.name)

            random_args = ''

            ctors = [method for method in obj.methods if method.name == obj.name]
            assert len(ctors)==1

            for i,arg in enumerate(ctors[0].args):
                tname = arg.TypeName()
                if arg.optional and arg.list:
                    random_arg = f'random_optional_list_{tname}()'
                elif arg.optional and not arg.list:
                    random_arg = f'random_optional_{tname}()'
                elif not arg.optional and arg.list:
                    random_arg = f'random_list_{tname}()'
                elif not arg.optional and not arg.list:
                    random_arg = f'random_{tname}()'
                else:
                    raise Exception('Development error')
                ending = '' if (i+1)==len(ctors[0].args) else ','
                random_args += f'{indent*2}{random_arg}{ending}\n'

            code_construct_random.extend(f'''
def random_{obj.name} ():
    return {obj.name} (
{random_args}
    )
'''.split('\n'))

            code_construct_random.extend(f'''
def random_optional_{obj.name} () -> {obj.name}|None:
    if yes_no():
        return None
    return random_{obj.name}()
'''.split('\n'))

            code_construct_random.extend(f'''
def random_list_{obj.name} (min:int = 0, max:int = 3) -> list[{obj.name}]:
    size = random.randint(min,max)
    return [random_{obj.name}() for i in range(size)]
'''.split('\n'))

            code_construct_random.extend(f'''
def random_optional_list_{obj.name} (min:int = 0, max:int = 3) -> list[{obj.name}]|None:
    if yes_no():
        return None
    return random_list_{obj.name}(min,max)
'''.split('\n'))

            code_create.append(f'''
        elif struct_name=='{obj.name}':
            obj1 = random_{obj.name}()
            open(file1_name,'w').write({obj.name}_to_json_string(obj1))
            obj2 = {obj.name}_from_json_string(open(file1_name).read())
            assert isinstance(obj1,{obj.name})
            assert isinstance(obj2,{obj.name})
            assert obj1==obj2
''')

            code_convert.extend(f'''
        elif struct_name=='{obj.name}':
            obj = {obj.name}_from_json_string(open(file1_name).read())
            open(file2_name,'w').write({obj.name}_to_json_string(obj))
'''.split('\n'))

            code_compare.extend(f'''
        elif struct_name=='{obj.name}':
            obj1 = {obj.name}_from_json_string(open(file1_name).read())
            obj2 = {obj.name}_from_json_string(open(file2_name).read())
            assert obj1==obj2
'''.split('\n'))

        test_template = '''
import sys, random, uuid
from dto import *

def random_string(len_max:int = 5) -> str:
    return str(uuid.uuid4())[0:random.randint(0,len_max)]

def random_list_string(min:int = 0, max:int = 3) -> list[str]:
    n = random.randint(min,max)
    return [random_string() for i in range(n)]

def random_optional_string (len_max:int=5) -> str|None:
    if yes_no(): return None
    return random_string()

def random_optional_list_string(min:int = 0, max:int = 3) -> list[str]:
    if yes_no(): return None
    return random_list_string(min,max)

def random_int (min = -1000, max = 1000) -> int:
    return random.randint(min,max)

def yes_no () -> bool:
    return random_int(0,1)

def random_optional_int (min = -1000, max = 1000) -> int:
    if yes_no(): return None
    return random_int(min,max)

def random_list_int(min:int = 0, max:int = 3) -> list[int]:
    n = random.randint(min,max)
    return [random_int() for i in range(n)]

def random_optional_list_int(min:int = 0, max:int = 3) -> list[int]|None:
    if yes_no(): return None
    return random_list_int(min,max)

def random_float (min:float = -1e6, max:float = 1e6) -> float:
    return random_int()
    # FIXME
    # return random.uniform(min,max)

def random_optional_float (min = -1e6, max = 1e6) -> float|None:
    if yes_no(): return None
    return random_int()
    # FIXME
    # return random.uniform(min,max)

def random_list_float (min:int = 0, max:int = 3) -> list[float]:
    n = random.randint(min,max)
    return [random_float() for i in range(n)]

def random_optional_list_float (min = 0, max = 3) -> list[float]|None:
    if yes_no(): return None
    return random_list_float(min,max)

#create-struct-random#

def test_round_trip_python(command, struct_name, file1_name, file2_name):
    if command=='build':
        return

    if command=='create':
        if False:
            pass
#create-struct-tests#
        else:
            raise Exception(f'Operation "{command}" does not supported struct {struct_name}')
    elif command=='convert':
        if False:
            pass
#convert-struct-tests#
        else:
            raise Exception(f'Operation "{command}" does not supported struct {struct_name}')
    elif command=='compare':
        if False:
            pass
#compare-struct-tests#
        else:
            raise Exception(f'Operation "{command}" does not supported struct {struct_name}')
    else:
        raise Exception(f'Not supported command {command}')
'''

        code = []
        for line in test_template.split('\n'):
            if line=='#create-struct-random#':
                code.extend(code_construct_random)
            elif line=='#create-struct-tests#':
                code.extend(code_create)
            elif line=='#convert-struct-tests#':
                code.extend(code_convert)
            elif line=='#compare-struct-tests#':
                code.extend(code_compare)
            else:
                code.append(line)
        return code

    def CreateTestEnv(self, objs, args):

        os.makedirs (self.GetDirTestEnv(args), exist_ok=True)

        ext_py = self.extension
        name = f'{self.name_dto}.{ext_py}'
        os.symlink(f'../../{self.name_dto}/{self.language}/{name}',f'{self.GetDirTest(args)}/{name}')
        os.symlink(f'../../{self.name_dto}/{self.language}/{name}',f'{self.GetDirTestEnv(args)}/{name}')
        name = f'{self.name_test}.{ext_py}'
        os.symlink(f'../../{self.name_test}/{self.language}/{name}',f'{self.GetDirTestEnv(args)}/{name}')

        run_python = f'''#!/usr/bin/env python3

from {self.name_dto}  import *
from {self.name_test} import *

if __name__ == '__main__':
    test_round_trip_python(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3],
        sys.argv[4] if len(sys.argv)>4 else ''
    )
'''

        run = f'''#!/usr/bin/env bash

case "$1" in
    build)
        ;;
    *)
        ./run-python $@
        ;;
esac
'''

        name = f'{self.GetDirTestEnv(args)}/run-python'
        with open(name,'w') as f:
            f.write(run_python)
        os.chmod(name,0o777)

        name = f'{self.GetDirTestEnv(args)}/run'
        with open(name,'w') as f:
            f.write(run)
        os.chmod(name,0o777)


class CodeTypescript (Code):
    def __init__ (self):
        super().__init__('typescript','ts')

class CodeCpp (Code):
    def __init__ (self):
        super().__init__('cpp','cpp')

def process (objs, lang:str, args):
    if lang=='cpp':
        g = CodeCpp()
    elif lang=='python':
        g = CodePython()
    elif lang=='typescript':
        g = CodeTypescript()
    else:
        raise NotImplementedError(f'process() has not support for "{lang}" language')

    g.Process(objs, args)
