from .all import *

def python_type_to_string (var:Variable) -> str:

    tname = var.TypeName()

    type_str = {
        'void'    : 'void',
        'string'  : 'str',
        'boolean' : 'bool',
        'int'     : 'int',
        'float'   : 'float',
    } .get(tname,tname)

    if var.list:
        type_str = f'list[{type_str}]'
    if var.optional:
        type_str = f'{type_str}|None'
    return type_str

def python_value_to_string (arg) -> str:
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

def File_prefix_python (objs)  -> list[str]:
    return f'''
# {autogen_text}
from copy import deepcopy
from math import nan
import json
from json import JSONEncoder

def _default(self, obj):
    return getattr(obj.__class__, "to_json", _default.default)(obj)

_default.default = JSONEncoder().default
JSONEncoder.default = _default

'''.split('\n')

def Constructor_python(ctor:Function,base:Struct) -> list[str]:

    assert ctor.name == base.name

    code = []
    code.append('')
    
    code.append(f'def __init__ (')
    code.append(f'{indent}self,')
    for i,arg in enumerate(ctor.args):
        defval = ''
        if arg.defval is not None:
            defval = f' = {python_value_to_string(arg.defval)}'
        elif arg.optional:
            defval = ' = None'
        else:
            defval = ''
        code.append(f'{indent}{arg.name}{defval}{"," if i+1<len(ctor.args) else ""}')
    code.append(f'):')

    for i,(name,mapping) in enumerate(ctor.mapping):
        if base.base and name==base.base.name:
            code.append(f'{indent}super().__init__(')
            for arg in mapping:
                code.append(f'{indent*2}{python_value_to_string(arg)},')
            code.append(f'{indent})')
        else:
            assert len(mapping)==1
            arg = mapping[0]

            attr = None
            for a in base.attributes:
                if a.name == name:
                    attr = a
            assert attr is not None
            if isinstance(attr.type,Struct) and isinstance(arg,Variable):# and isinstance(arg.defval,Struct):
                code.append(f'{indent*1}self.{attr.name} : {python_type_to_string(attr)} = deepcopy({python_value_to_string(arg)})')
            else:
                code.append(f'{indent*1}self.{attr.name} : {python_type_to_string(attr)} = {python_value_to_string(arg)}')

    return code

def Function_python(self:Function, obj:Struct=None) -> list[str]:
    code = []

    if obj and self.name==obj.name:
        code = Constructor_python(self,obj)
    else:
        code = []
        code.append(f'def {self.name} (')
        if obj:
            code.append(f'{indent}self,')

        for a in self.args:
            default = '' if a.defval is None else f' = {python_value_to_string(a.defval)}'
            code.append(f'{indent}{a.name}{default}')
        code.append('):')

    for line in get_code(self.code.get('python')):
        code.append(f'{indent}{line}')

    code.append(f'{indent}pass')
    return code

def Struct_python (self:Struct) -> list[str]:
    code = []
    if self.base:
        code.append(f'class {self.name} ({self.base.name}):')
    else:
        code.append(f'class {self.name}:')
    code.append('')
    
    for func in self.methods:
        for line in Function_python(func,self):
            code.append(f'{indent}{line}')
        code.append('')

    code.append(f'{indent}def __eq__ (self, other):')
    if self.base:
        code.append(f'{indent*2}if not super().__eq__(other): return False')
    for attr in self.attributes:
        code.append(f'{indent*2}if self.{attr.name} != other.{attr.name}: return False')
    code.append(f'{indent*2}return True')

    code.append(f'{indent}def __neq__ (self, other):')
    code.append(f'{indent*2}return not self==other')

    code.extend(Struct_from_json_string_python(self))
    code.extend(Struct_to_json_string_python(self))

    code.extend(Struct_from_json_python(self))
    code.extend(Struct_to_json_python(self))

    return code

def Struct_to_json_python (self:Struct) -> list[str]:
    code = []
    code.append(f'def {self.name}_to_json(j:dict, obj:{self.name}):')
    if self.base:
        code.append(f'{indent}{self.base.name}_to_json(j,obj)')
    for attr in self.attributes:
        if attr.skip_dto: continue
        var_code = []
        if isinstance(attr.type,str):
            var_code.append(f'j["{attr.name}"] = obj.{attr.name}')
        elif isinstance(attr.type,Struct) and not attr.list:
            var_code.append(f'jj = {{}}')
            var_code.append(f'{attr.TypeName()}_to_json(jj,obj.{attr.name})')
            var_code.append(f'j["{attr.name}"] = jj')
        elif isinstance(attr.type,Struct) and attr.list:
            var_code.append(f'j["{attr.name}"] = []')
            var_code.append(f'for item in obj.{attr.name}:')
            var_code.append(f'{indent}jj = {{}}')
            var_code.append(f'{indent}{attr.TypeName()}_to_json(jj,item)')
            var_code.append(f'{indent}j["{attr.name}"].append(jj)')
        else:
            raise NotImplementedError()
        if attr.optional:
            code.append(f'{indent*1}if obj.{attr.name} is not None:')
            for line in var_code:
                code.append(f'{indent*2}{line}')
        else:
            for line in var_code:
                code.append(f'{indent*1}{line}')
    if not code:
        code.append(f'{indent}pass')
    code.append('')
    return code

def Struct_to_json_string_python (self:Struct) -> list[str]:
    code = []
    code.append(f'def {self.name}_to_json_string (self:{self.name}):')
    code.append(f'{indent}j = {{}}')
    code.append(f'{indent}{self.name}_to_json(j,self)')
    code.append(f'{indent}return json.dumps(j)')
    return code

def Struct_from_json_python (self) -> list[str]:
    code = []

    code.append(f'def {self.name}_from_json (j:dict, obj:{self.name}):')
    code.append(f'{indent}assert isinstance(obj,{self.name})')
    if self.base:
        code.append(f'{indent}{self.base.name}_from_json(j,obj)')

    for attr in self.attributes:
        if attr.skip_dto: continue
        if isinstance(attr.type,Struct):
            if attr.optional and not attr.list:
                code.append(f'{indent*1}if j.get("{attr.name}",None) is not None:')
                # code.append(f'{indent*2}jj = ')
                code.append(f'{indent*2}{attr.TypeName()}_from_json(j["{attr.name}"],obj.{attr.name})')
                # code.append(f'{indent*2}obj.{attr.name} = jj')
                code.append(f'{indent*1}else:')
                code.append(f'{indent*2}obj.{attr.name} = None')
            elif not attr.optional and attr.list:
                code.append(f'{indent*1}for item in j["{attr.name}"]:')
                code.append(f'{indent*2}v = {attr.TypeName()}()')
                code.append(f'{indent*2}{attr.TypeName()}_from_json(item,v)')
                code.append(f'{indent*2}obj.{attr.name}.append(v)')
            else:
                code.append(f'{indent}{attr.TypeName()}_from_json(j["{attr.name}"],obj.{attr.name})')
        else:
            if attr.optional:
                code.append(f'{indent}obj.{attr.name} = j.get("{attr.name}",None)')
            else:
                code.append(f'{indent}obj.{attr.name} = j["{attr.name}"]')

    return code

def Struct_from_json_string_python (self) -> list[str]:
    code = []
    code.append(f'def {self.name}_from_json_string (jstr):')
    code.append(f'{indent}j = json.loads(jstr)')
    code.append(f'{indent}obj = {self.name}()')
    code.append(f'{indent}{self.name}_from_json(j,obj)')
    code.append(f'{indent}return obj')
    code.append('')
    return code

def Tests_python (objs) -> list[str]:

    struct_names = []
    code_construct_random = []
    code_create = []
    code_convert = []
    code_compare = []

    for obj in objs:
        if not isinstance(obj,Struct):
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
def random_list_{obj.name} (min:int = 0, max:int = 3):
    size = random.randint(min,max)
    return [random_{obj.name}() for i in range(size)]
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

    code = []
    for line in python_test_template.split('\n'):
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

python_test_template = '''
import sys, random, uuid
from output.dto import *

def random_string(len_max=5):
    return str(uuid.uuid4())[0:random.randint(0,len_max)]

def random_list_string(min = 0, max = 3):
    n = random.randint(min,max)
    return [random_string() for i in range(n)]

def random_int (min = -1000, max = 1000):
    return random.randint(min,max)

def random_list_int(min = 0, max = 3):
    n = random.randint(min,max)
    return [random_int() for i in range(n)]

def random_optional_list_int(min = 0, max = 3):
    if random.randint(0,1): return None
    n = random.randint(min,max)
    return [random_int() for i in range(n)]

def random_float (min = -1e6, max = 1e6):
    return random_int()
    # FIXME
    # return random.uniform(min,max)

def random_optional_float (min = -1e6, max = 1e6):
    if random.randint(0,1): return None
    return random_int()
    # FIXME
    # return random.uniform(min,max)

def random_list_float (min = 0, max = 3):
    n = random.randint(min,max)
    return [random_float() for i in range(n)]

def random_optional_list_float (min = 0, max = 3):
    if random.randint(0,1): return None
    n = random.randint(min,max)
    return [random_float() for i in range(n)]

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