from .all import *
import math

def csharp_type_to_string (name:str):

    if name[-2:]=='[]':
        t = csharp_type_to_string(name[:-2])
        return f'List<{t}>'

    return {
        'void'    : 'void',
        'string'  : 'string',
        'int'     : 'int',
        'float'   : 'float',
    }.get(name,name)

def csharp_value_to_string (arg):
    if type(arg)==Variable:
        return arg.name
    elif isinstance(arg,list):
        x = [ f'{item.name}'   for item in arg]
        y = ','.join(x)
        return f'{{{y}}}'
    elif isinstance(arg,str):
        return f'"{arg}"'
    elif type(arg)==float:
        if math.isnan(arg):
            return 'float.NAN'
        else:
            return str(arg)
    else:
        return str(arg)

def Constructor_csharp(ctor:Function,base:Struct):
    code = []
    code.append(f'// Constructor_csharp {ctor.name}')
    return code

def Function_csharp(self:Function, obj:Struct=None):
    code = []
    code.append(f'// Function_csharp {self.name}')
    return code

def Struct_csharp (self:Struct):
    code = []
    if self.base:
        code.append(f'public class {self.name}: {self.base.name} {{')
    else:
        code.append(f'public class {self.name} {{')
    code.append(f'')
    
    for a in self.attributes:
        code.append(f'{indent}public {csharp_type_to_string(a.type)} {a.name};')

    code.append('')

    for func in self.methods:
        for line in Function_csharp(func,self):
            code.append(f'{indent}{line}')
        code.append('')

    # FIXME
    # code.extend(Struct_compare_cpp(self))

    code.append(f'}};')

    # FIXME
    # if self.generate_json:
    #     code.extend(Struct_to_JSON_cpp(self))
    #     code.extend(Struct_to_JSON_string_cpp(self))
    #     code.extend(Struct_from_JSON_cpp(self))
    #     code.extend(Struct_from_JSON_string_cpp(self))

    return code
