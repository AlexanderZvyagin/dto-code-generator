from .all import *
import math

def typescript_type_to_string (name:str):

    if name[-2:]=='[]':
        t = typescript_type_to_string(name[:-2])
        return f'{t}[]'

    return {
        'void'    : 'void',
        'string'  : 'string',
        'int'     : 'number',
        'float'   : 'number',
    }.get(name,name)

def typescript_value_to_string (arg):
    if type(arg)==Variable:
        if arg.type=='type':
            return f'new {arg.name}'
        else:
            return arg.name
    elif isinstance(arg,list):
        x = [ f'{item.name}'   for item in arg]
        y = ','.join(x)
        return f'[{y}]'
    elif isinstance(arg,str):
        return f'"{arg}"'
    elif type(arg)==float:
        if math.isnan(arg):
            return 'Number.NaN'
        else:
            return str(arg)
    else:
        return str(arg)


def File_prefix_typescript (objs):
    return [
        f'// {autogen_text}',
        ''
    ]

# def File_suffix_typescript (objs):
#     code = []
#     code.append('export {')
#     for i,obj in enumerate(objs):
#         c = ',' if (i+1)<len(objs) else ''
#         code.append(f'{indent}{obj.name}' + c)
#     code.append('}')
#     return code

# def typescript_type (name:str):
#     return {
#         'void'   : 'void',
#         'string' : 'string',
#         'int'    : 'number',
#         'int[]'  : 'number[]',
#         'float'  : 'number',
#         'float[]': 'number[]',
#     }.get(name,name)

# def typescript_value (arg):
#     if type(arg)==float:
#         if math.isnan(arg):
#             return 'Number.NaN'
#     return arg

def Constructor_typescript(ctor:Function,base:Struct):
    code = []
    code.append(f'constructor(')

    for arg in ctor.args:
        defval = '' if arg.defval is None else f' = {typescript_value_to_string(arg.defval)}'
        code.append(f'{indent}{arg.name} : {typescript_type_to_string(arg.type)} {defval},')
    code.append('){')

    for name,mapping in ctor.mapping:
        if base.base and base.base.name == name:
            code.append(f'{indent}super(')
            for v in mapping:
                code.append(f'{indent*2}{typescript_value_to_string(v)},')
            code.append(f'{indent});')
        else:
            assert len(mapping)==1
            code.append(f'{indent}this.{name} = {typescript_value_to_string(mapping[0])};')

    code.append(f'')
    return code

def Function_typescript (self:Function, obj:Struct=None):

    code = []

    if obj and self.name==obj.name:
        code = Constructor_typescript(self,obj)
    else:
        ftype = typescript_type_to_string(self.type)+' '

        code = []
        code.append(f'{self.name} (')

        for a in self.args:
            code.append(f'{indent}')
            default = '' if a.defval is None else f' = {typescript_value_to_string(a.defval)}'
            code.append(f'{indent}{a.name} : {typescript_type_to_string(a.type)}{default},')
        code.append(f') : {ftype} {{')

    for line in get_code(self.code.get('typescript')):
        code.append(f'{indent}{line}')
    code.append('}')

    return code

def Struct_typescript (self:Struct):
    code = []
    if self.base:
        code.append(f'class {self.name} extends {self.base.name} {{')
    else:
        code.append(f'class {self.name} {{')
    code.append(f'')
    
    for a in self.attributes:
        code.append(f'{indent}{a.name} : {typescript_type_to_string(a.type)};')

    code.append('')

    for func in self.methods:
        for line in Function_typescript(func,self):
            code.append(f'{indent}{line}')
        code.append('')

    # FIXME
    # code.extend(Struct_compare_typescript(self))

    code.append(f'}}')

    # FIXME
    # if self.generate_json:
    #     code.extend(Struct_to_JSON_cpp(self))
    #     code.extend(Struct_to_JSON_string_cpp(self))
    #     code.extend(Struct_from_JSON_cpp(self))
    #     code.extend(Struct_from_JSON_string_cpp(self))

    return code
