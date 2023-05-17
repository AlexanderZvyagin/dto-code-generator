from .all import *

experimental_version = 1

'''

There are two things to generate:

The generator interface does not know:
- how many files will be generated
- what are the file names, the purpose of files

yield {'directory':outdir,'file':file_name,'line':code_line}
yield {'path':relative_path,'line':code_line}
'''
class Generator:
    def __init__ (self, language, extension):
        self.language = language
        self.extension = extension

    def Process (self, objs, args):
        # outdir = args.get('dir_dto')
        # if outdir: self.ProcessDto(objs, outdir)
        self.ProcessDto(objs, args)

        print(f'experimental_version={experimental_version}')
        self.ProcessTestsSingleFile(objs, args)
        # outdir = args.get('dir_tests')
        # if outdir: self.ProcessTests(objs, outdir)

        # outdir = args.get('dir_run_tests')
        # if outdir: self.ProcessRunTests(objs, outdir)

    def ProcessDtoSingleFilePrefix (self, args):
        return []

    def ProcessDtoSingleFileSuffix (self, args):
        return []

    def ProcessDtoSingleFile (self, objs, args):
        outdir = args.get('dir_dto')
        if not outdir: return

        name = f'{outdir}/dto.{self.extension}'

        with open(name,'w') as file:

            for line in self.ProcessDtoSingleFilePrefix(args):
                file.write(line+'\n')
            file.write('\n')

            for obj in objs:
                if isinstance(obj,Struct):
                    for line in self.StructCode(obj):
                        file.write(line+'\n')
                    file.write('\n')
                elif isinstance(obj,Function):
                    for line in self.FunctionCode(obj):
                        file.write(line+'\n')
                    file.write('\n')
                elif isinstance(obj,CodeBlock):
                    for line in obj.code.get(self.language,[]):
                        file.write(line+'\n')
                else:
                    print(f'Cannot handle {type(obj)}')

            schema_version = args.get('schema_version')
            if schema_version:
                for line in self.ProcessDtoSingleFileSuffix(schema_version):
                    file.write(line+'\n')
                file.write('\n')

    def ProcessDto(self, objs, args):
        print(f'Code is missing for: ProcessDto {self.language}')

    def ProcessTests(self, objs, outdir):
        print(f'Code is missing for: ProcessTests {self.language}')

    # def ProcessRunTests(self, objs, outdir):
    #     print(f'Code is missing for: ProcessRunTests {self.language}')

    def StructCode (self, obj):
        print(f'Code is missing for: StructCode {self.language}')
        return []

    def FunctionCode (self, func:Function, obj:Struct=None):
        print(f'Code is missing for: FunctionCode {self.language}')
        return []

    def ConstructorCode(self, ctor:Function, base:Struct=None):
        print(f'Code is missing for: ConstructorCode {self.language}')
        return []

    def StructFromJson (self, obj:Struct):
        return []

    def StructToJson (self, obj:Struct):
        return []

    def StructFromJsonString (self, obj:Struct):
        return []

    def StructToJsonString (self, obj:Struct):
        return []

    def ProcessTestsSingleFile (self, objs, args):
        print('----------------------')
        outdir = args.get('dir_tests')
        print('aqqqqq',outdir)
        if not outdir: return
        name = f'{outdir}/{self.name_test}.{self.extension}'
        print(f'AAAAAAAAAAAAAAAAAAAAAAAAA!!!!! {name}')
        with open(name,'w') as file:
            for line in self.ProcessTests(objs):
                yield line

class GeneratorCpp (Generator):
    def __init__ (self):
        super().__init__ ('cpp','cpp')

'''
Python code generator

It generates two files: the dto file and the test file.
'''
class GeneratorPython (Generator):

    def __init__ (self):
        super().__init__ ('python','py')

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

    def ProcessDto(self, objs, args):
        # outdir = args.get('dir_dto')
        # if outdir: self.ProcessDtoSingleFile(objs, outdir)
        self.ProcessDtoSingleFile(objs, args)

    def StructCode (self, obj:Struct):

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
            for line in self.FunctionCode(func,obj):
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

        for line in self.StructFromJsonString(obj):
            yield line
        for line in self.StructToJsonString(obj):
            yield line
        # code.extend(Struct_from_json_string_python(self))
        # code.extend(Struct_to_json_string_python(self))

        for line in self.StructFromJson(obj):
            yield line
        for line in self.StructToJson(obj):
            yield line
        # code.extend(Struct_from_json_python(self))
        # code.extend(Struct_to_json_python(self))

    def FunctionCode(self, func:Function, base:Struct=None) -> list[str]:
        if base and func.name==base.name:
            for line in self.ConstructorCode(func,base):
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

    def ConstructorCode(self, ctor:Function, base:Struct=None):
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

    def ProcessDtoSingleFilePrefix (self, args):
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

    def StructFromJson (self, obj:Struct):
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

    def StructFromJsonString (self, obj:Struct):
        yield f'def {obj.name}_from_json_string (jstr):'
        yield f'{indent}j = json.loads(jstr)'
        yield f'{indent}obj = {obj.name}()'
        yield f'{indent}{obj.name}_from_json(j,obj)'
        yield f'{indent}return obj'
        yield ''

    def StructToJson (self, obj:Struct):
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
            # code.extend([f'{indent*n}{line}' for line in code_not_optional])
        # FIXME?!
        yield f'{indent}pass'
        yield ''

    def StructToJsonString (self, obj:Struct):
        yield f'def {obj.name}_to_json_string (self:{obj.name}):'
        yield f'{indent}j = {{}}'
        yield f'{indent}{obj.name}_to_json(j,self)'
        yield f'{indent}return json.dumps(j)'

    def TestsCode (self, objs):

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

        for line in test_template.split('\n'):
            if line=='#create-struct-random#':
                for code_line in code_construct_random:
                    yield code_line
            elif line=='#create-struct-tests#':
                for code_line in code_create:
                    yield code_line
            elif line=='#convert-struct-tests#':
                for code_line in code_convert:
                    yield code_line
            elif line=='#compare-struct-tests#':
                for code_line in code_compare:
                    yield code_line
            else:
                yield line


class GeneratorTypescript (Generator):
    def __init__ (self):
        super().__init__ ('typescript','ts')

def process (objs, lang, args):
    if lang=='cpp':
        g = GeneratorCpp()
    elif lang=='python':
        g = GeneratorPython()
    elif lang=='typescript':
        g = GeneratorTypescript()
    else:
        raise NotImplemented

    g.Process(objs, args)
