from .all import *

def python_type_to_string (var:Variable):

    type_str = {
        'void'    : 'void',
        'string'  : 'str',
        'int'     : 'int',
        'float'   : 'float',
    } .get(var.type,var.type)

    if var.list:
        type_str = f'list[{type_str}]'
    if var.optional:
        type_str = f'{type_str}|None'
    return type_str

def python_value_to_string (arg):
    if type(arg)==Variable:
        return arg.name
    elif isinstance(arg,list):
        x = [ f'{item.name}'   for item in arg]
        y = ','.join(x)
        return f'[{y}]'
    elif type(arg)==str:
        return f'"{arg}"'
    else:
        return str(arg)

def File_prefix_python (objs):
    return [
        f'# {autogen_text}',
        'from math import nan',
        'import json',
        '# 1',
        ''
    ]

def Constructor_python(ctor:Function,base:Struct):

    assert ctor.name == base.name

    code = []
    code.append('')
    
    code.append(f'def __init__ (')
    code.append(f'{indent}self,')
    for i,arg in enumerate(ctor.args):
        # defval = '' if arg.defval is None else f' = {python_value_to_string(arg.defval)}'
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

            # if attr.optional:
            #     code.append(f'{indent*1}if {python_value_to_string(arg)} is not None:')
            #     code.append(f'{indent*2}self.{attr.name} : {python_type_to_string(attr)} = {python_value_to_string(arg)}')
            # else:
            code.append(f'{indent*1}self.{attr.name} : {python_type_to_string(attr)} = {python_value_to_string(arg)}')

    return code

def Function_python(self:Function, obj:Struct=None):
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

def Struct_python (self:Struct):
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
    code.append(f'{indent*2}return not (self==other)')

    if self.generate_json:
        code.extend(Struct_to_json_string_python(self))
        code.extend(Struct_from_json_string_python(self))

    return code

def Struct_to_json_string_python (self:Struct):
    code = []
    code.append(f'def {self.name}_to_json_string (self):')
    optional_attributes = [attr.name for attr in self.attributes if attr.optional]
    code.append(f'{indent}return json.dumps(self,default=lambda x: {{k:v for k,v in x.__dict__.items() if not (k in {optional_attributes} and v is None) }})')
    return code

def Struct_from_json_string_python (self):
    code = []

    code.append(f'def {self.name}_from_json (j, obj):')
    if self.base:
        code.append(f'{indent}{self.base.name}_from_json(j,obj)')
    for attr in self.attributes:
        # TODO
        if attr.name[0]=='_': continue
        if attr.optional:
            code.append(f'{indent}obj.{attr.name} = j.get("{attr.name}",None)')
        else:
            code.append(f'{indent}obj.{attr.name} = j["{attr.name}"]')
    # code.append(f'{indent}return')

    code.append(f'def {self.name}_from_json_string (jstr):')
    code.append(f'{indent}j = json.loads(jstr)')
    code.append(f'{indent}obj = {self.name}()')
    code.append(f'{indent}{self.name}_from_json(j,obj)')
    code.append(f'{indent}return obj')
    code.append('')
    return code

def Tests_python (objs):

    struct_names = []
    code_construct_random = []
    code_create = []
    code_convert = []
    code_compare = []

    for obj in objs:
        if type(obj)!=Struct:
            continue

        struct_names.append(obj.name)

        random_args = ''

        ctors = [method for method in obj.methods if method.name == obj.name]
        assert len(ctors)==1

        for i,arg in enumerate(ctors[0].args):
            if arg.optional:
                if arg.list:
                    if arg.type=='string':
                        random_arg = 'random_optional_list_of_strings()'
                    elif arg.type=='float':
                        random_arg = 'random_optional_list_of_floats()'
                    elif arg.type=='int':
                        random_arg = 'random_optional_list_of_ints()'
                    elif arg.type in struct_names:
                        random_arg = f'random_optional_list_of_{arg.type}()'
                    else:
                        raise Exception(f'Unknown type {arg.type}')
                elif arg.type=='string':
                    random_arg = 'random_optional_string()'
                elif arg.type=='float':
                    random_arg = 'random_optional_float()'
                elif arg.type=='int':
                    random_arg = 'random_optional_int()'
                elif arg.type in struct_names:
                    random_arg = f'random_optional_{arg.type}()'
                else:
                    raise Exception(f'Unknown type {arg.type}')
            else:
                if arg.list:
                    if arg.type=='string':
                        random_arg = 'random_list_of_strings()'
                    elif arg.type=='float':
                        random_arg = 'random_list_of_floats()'
                    elif arg.type=='int':
                        random_arg = 'random_list_of_ints()'
                    elif arg.type in struct_names:
                        random_arg = f'random_list_of_{arg.type}()'
                    else:
                        raise Exception(f'Unknown type {arg.type}')
                elif arg.type=='string':
                    random_arg = 'random_string()'
                elif arg.type=='float':
                    random_arg = 'random_float()'
                elif arg.type=='int':
                    random_arg = 'random_int()'
                elif arg.type in struct_names:
                    random_arg = f'random_{arg.type}()'
                else:
                    raise Exception(f'Unknown type {arg.type}')
            ending = '' if (i+1)==len(ctors[0].args) else ','
            random_args += f'{indent*2}{random_arg}{ending}\n'

        code_construct_random.extend(f'''
def random_{obj.name} ():
    return {obj.name} (
{random_args}
    )
'''.split('\n'))

        code_construct_random.extend(f'''
def random_list_of_{obj.name} (min:int = 0, max:int = 3):
    size = random.randint(min,max)
    return [random_{obj.name}() for i in range(size)]
'''.split('\n'))

        code_create.append(f'''
        elif struct_name=='{obj.name}':
            obj = {obj.name}_to_json_string(random_{obj.name}())
            open(file1_name,'w').write(obj)
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

def random_list_of_strings(min = 0, max = 3):
    n = random.randint(min,max)
    return [random_string() for i in range(n)]

def random_int (min = -1000, max = 1000):
    return random.randint(min,max)

def random_list_of_ints(min = 0, max = 3):
    n = random.randint(min,max)
    return [random_int() for i in range(n)]

def random_optional_list_of_ints(min = 0, max = 3):
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

def random_list_of_floats (min = 0, max = 3):
    n = random.randint(min,max)
    return [random_float() for i in range(n)]

def random_optional_list_of_floats (min = 0, max = 3):
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