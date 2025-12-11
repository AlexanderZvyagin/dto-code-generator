import os, logging
from .all import *
from .Code import *

logger = logging.getLogger(__name__)

class CodePython (Code):
    def __init__ (self, options={}):
        super().__init__('python','py',options)

    def Skip (self, obj):
        if isinstance(obj,Struct):
            return not obj.default_version
        else:
            return False

    def TypeToString (self, var:Variable|str) -> str:

        m = {
            BasicType.null    : 'void',
            BasicType.string  : 'str',
            BasicType.boolean : 'bool',
            BasicType.int     : 'int',
            BasicType.float   : 'float',
        }

        if type(var)==Variable:
            tname = var.TypeName()
        else:
            tname = var

        kv = detect_dict_key_value(tname)
        if kv:
            tname = f'dict[{m.get(kv[0],kv[0])},{m.get(kv[1],kv[1])}]'

        type_str = m.get(tname,tname)

        if type(var)==Variable:
            if var.list:
                type_str = f'list[{type_str}]'
            if var.optional:
                type_str = f'{type_str}|None'
            # if var.variant:
            #     assert tname=='variant'
            #     raise Exception(f'Variant is not supported: {var.variant}')

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

    def GeneratorDto (self, objs):
        path = f'{self.GetDirDto()}/{self.name_dto}.{self.extension}'

        for line in self.GeneratorSingleDtoFilePrefix (objs):
            yield (path, line)

        for line in self.GeneratorSingleDtoFileBody   (objs):
            yield (path, line)

        for line in self.GeneratorSingleDtoFileSuffix (objs):
            yield (path, line)

    def GeneratorTests (self, objs):
        path = f'{self.GetDirTest()}/{self.name_test}.{self.extension}'

        for line in self.GeneratorTest (objs):
            yield (path, line)

    def GeneratorSingleDtoFilePrefix (self, objs):
        schema_version = self.options.get('schema_version')
        if schema_version:
            for line in autogen_text(schema_version).split('\n'):
                yield f'# {line}'

        code = f'''
from __future__ import annotations
from copy import deepcopy
import math
from math import nan
import json

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

    def GeneratorSingleDtoFileSuffix (self, objs):
        return ()

    def GeneratorSingleDtoFileBody (self, objs):
        for obj in objs:
            if self.Skip(obj):
                continue
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
            elif isinstance(obj,Include):
                includes_dir = self.options.get('schema_includes_dir','.')
                separation_line = '#'*32
                for file in obj.files.get(self.language,[]):
                    yield separation_line
                    yield f'# The start of "{file}"'
                    yield separation_line
                    for line in open(f'{includes_dir}/{file}').readlines():
                        yield line.rstrip('\n')
                    yield separation_line
                    yield f'# The end of "{file}"'
                    yield separation_line
                yield ''
            else:
                logger.error(f'Cannot handle {type(obj)}')

    def GenerateDocString(self, doc):
        yield f"{indent}'''"
        for line in doc.splitlines():
            yield line
        yield "'''"

    def GeneratorStruct (self, obj:Struct):

        yield f'# Forward declaration'
        yield f'class {obj.name}: pass'

        if obj.base:
            yield f'class {obj.name} ({obj.base.name}):'
        else:
            yield f'class {obj.name}:'
        yield ''

        if obj.doc:
            yield ''
            for line in self.GenerateDocString(obj.doc):
                yield line
            yield ''

        for attr in obj.attributes:
            if attr.static:
                assert attr.defval is not None
                yield f'{indent}{attr.name} : {self.TypeToString(attr)} = {self.ValueToString(attr.defval)}'

        for func in obj.methods:
            if func.type=='constructor' or func.code.get(self.language):
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

        for line in self.GeneratorStructFromJson(obj):
            yield line
        for line in self.GeneratorStructToJson(obj):
            yield line

    def GeneratorFunction (self, func:Function, base:Struct=None):

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
            yield f') -> {self.TypeToString(func.ReturnType())} :'

            if func.doc:
                yield ''
                for line in self.GenerateDocString(func.doc):
                    yield line
                yield ''

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
            elif type(arg.type)==Struct:
                defval = f' = {arg.type.name}()'
            else:
                defval = ''
            yield f'{indent}{arg.name}:{self.TypeToString(arg)}{defval}{"," if i+1<len(ctor.args) else ""}'
        yield f'):'

        if ctor.doc:
            yield ''
            for line in self.GenerateDocString(ctor.doc):
                yield line
            yield ''

        def init_attr (attr, value):
            if isinstance(attr.type,Struct) and isinstance(value,Variable):
                return f'{indent*1}self.{attr.name} : {self.TypeToString(attr)} = deepcopy({self.ValueToString(value)})'
            else:
                return f'{indent*1}self.{attr.name} : {self.TypeToString(attr)} = {self.ValueToString(value)}'

        for attr in base.attributes:
            if attr.defval is not None:
                yield init_attr(attr,attr.defval)

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
                if attr.doc:
                    for line in attr.doc.splitlines():
                        line = line.strip()
                        if line:
                            yield f'{indent*1}#: {line}'
                yield init_attr(attr,arg)

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

    def GeneratorTest (self, objs):

        struct_names = []
        code_construct_random = []
        code_create = []
        code_convert = []
        code_compare = []

        for obj in objs:
            if self.Skip(obj):
                continue
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
    if random_boolean():
        return None
    return random_{obj.name}()
'''.split('\n'))

            code_construct_random.extend(f'''
def random_list_{obj.name} (min:int = 0, max:int = 3) -> list[{obj.name}]:
    global recursionDepth, maxRecursionDepth
    lst = []
    if recursionDepth<maxRecursionDepth:
        recursionDepth += 1
        size = random.randint(min,max)
        lst = [random_{obj.name}() for i in range(size)]
        recursionDepth += 1
    return lst
'''.split('\n'))

            code_construct_random.extend(f'''
def random_optional_list_{obj.name} (min:int = 0, max:int = 3) -> list[{obj.name}]|None:
    if random_boolean():
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
from __future__ import annotations
import sys, random, uuid
from dto import *

recursionDepth = 0
maxRecursionDepth = 5

def random_int (min = -1000, max = 1000) -> int:
    return random.randint(min,max)

def random_boolean () -> bool:
    return random_int(0,1)

def random_optional_int (min = -1000, max = 1000) -> int|None:
    if random_boolean(): return None
    return random_int(min,max)

def random_optional_boolean () -> bool|None:
    return random_int(0,1)

def random_list_int(min:int = 0, max:int = 3) -> list[int]:
    n = random.randint(min,max)
    return [random_int() for i in range(n)]

def random_optional_list_int(min:int = 0, max:int = 3) -> list[int]|None:
    if random_boolean(): return None
    return random_list_int(min,max)

def random_string(len_max:int = 5) -> str:
    return str(uuid.uuid4())[0:random.randint(0,len_max)]

def random_list_string(min:int = 0, max:int = 3) -> list[str]:
    n = random.randint(min,max)
    return [random_string() for i in range(n)]

def random_optional_string (len_max:int=5) -> str|None:
    if random_boolean(): return None
    return random_string()

def random_optional_list_string(min:int = 0, max:int = 3) -> list[str]:
    if random_boolean(): return None
    return random_list_string(min,max)

def random_float (min:float = -1e6, max:float = 1e6) -> float:
    return random_int()
    # FIXME
    # return random.uniform(min,max)

def random_optional_float (min = -1e6, max = 1e6) -> float|None:
    if random_boolean(): return None
    return random_int()
    # FIXME
    # return random.uniform(min,max)

def random_list_float (min:int = 0, max:int = 3) -> list[float]:
    n = random.randint(min,max)
    return [random_float() for i in range(n)]

def random_optional_list_float (min = 0, max = 3) -> list[float]|None:
    if random_boolean(): return None
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

    def CreateTestEnv(self, objs):

        os.makedirs (self.GetDirTestEnv(), exist_ok=True)

        ext_py = self.extension
        name = f'{self.name_dto}.{ext_py}'
        os.symlink(f'../../{self.name_dto}/{self.language}/{name}',f'{self.GetDirTest()}/{name}')
        os.symlink(f'../../{self.name_dto}/{self.language}/{name}',f'{self.GetDirTestEnv()}/{name}')
        name = f'{self.name_test}.{ext_py}'
        os.symlink(f'../../{self.name_test}/{self.language}/{name}',f'{self.GetDirTestEnv()}/{name}')

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

        name = f'{self.GetDirTestEnv()}/run-python'
        with open(name,'w') as f:
            f.write(run_python)
        os.chmod(name,0o777)

        name = f'{self.GetDirTestEnv()}/run'
        with open(name,'w') as f:
            f.write(run)
        os.chmod(name,0o777)
        
        self.test_environment_ready = True

register(CodePython)
