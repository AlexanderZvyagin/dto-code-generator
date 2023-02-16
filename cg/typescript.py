from .all import *
import math

def typescript_type_to_string (var:Variable):

    type_str = {
        'void'    : 'void',
        'string'  : 'string',
        'int'     : 'number',
        'float'   : 'number',
    } .get(var.type,var.type)

    if var.list:
        type_str = f'{type_str}[]'
    if var.optional:
        type_str = f'{type_str}|undefined'
    return type_str

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

def File_suffix_typescript (objs):
    code = []
    code.append('export {')
    for obj in objs:
        if type(obj) in [Struct,Function]:
            code.append(f'{indent}{obj.name},')
    code.append('}')
    return code

def Constructor_typescript(ctor:Function,base:Struct):
    code = []
    code.append(f'constructor(')

    for arg in ctor.args:
        defval = '' if arg.defval is None else f' = {typescript_value_to_string(arg.defval)}'
        code.append(f'{indent}{arg.name} : {typescript_type_to_string(arg)} {defval},')
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
        ftype = typescript_type_to_string(Variable('',self.type))+' '

        code = []
        code.append(f'{self.name} (')

        for a in self.args:
            code.append(f'{indent}')
            default = '' if a.defval is None else f' = {typescript_value_to_string(a.defval)}'
            code.append(f'{indent}{a.name} : {typescript_type_to_string(a)}{default},')
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
        code.append(f'{indent}{a.name} : {typescript_type_to_string(a)};')

    code.append('')

    for func in self.methods:
        for line in Function_typescript(func,self):
            code.append(f'{indent}{line}')
        code.append('')

    code.append(f'}}')

    return code

def Tests_typescript (objs):

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
function random_{obj.name} () : {obj.name} {{
    return new {obj.name} (
{random_args}
    );
}}
'''.split('\n'))

        code_construct_random.extend(f'''
function random_list_of_{obj.name} (min:number = 0, max:number = 3) : {obj.name}[] {{
    const size:number = Math.floor(min + Math.random()*(max-min));
    const list:{obj.name}[] = [];
    for(let i=0; i<size; i++)
        list.push(random_{obj.name}());
    return list;
}}
'''.split('\n'))

        code_create.append(f'''
    }} else if (struct_name === '{obj.name}') {{
        fs.writeFileSync(
            file_name,
            JSON.stringify (random_{obj.name}()));
''')

        code_convert.extend(f'''
    }} else if (struct_name === '{obj.name}') {{
        const obj = JSON.parse((fs.readFileSync(file1_name,'utf-8')));
        fs.writeFileSync(file2_name, JSON.stringify(obj));
'''.split('\n'))
        code_compare.extend(f'''
    }} else if (struct_name === '{obj.name}') {{
        const obj1 = JSON.parse((fs.readFileSync(file1_name,'utf-8')));
        const obj2 = JSON.parse((fs.readFileSync(file2_name,'utf-8')));
        if(!object_equals(obj1,obj2))
            throw new Error(`${{struct_name}} objects are not equal.`);
'''.split('\n'))

    code = []
    for line in typescript_test_template.split('\n'):
        if line=='//structs//':
            code.extend([f'{indent}{name},' for name in struct_names])
        elif line=='//create-struct-random//':
            code.extend(code_construct_random)
        elif line=='//create-struct-tests//':
            code.extend(code_create)
        elif line=='//convert-struct-tests//':
            code.extend(code_convert)
        elif line=='//compare-struct-tests//':
            code.extend(code_compare)
        else:
            code.append(line)
    return code

typescript_test_template = '''
// This file was automatically generated!
// - by <software> <version>
// - from <DTO-s spec>

import * as fs from 'fs'
import {
//structs//
} from './dto'

function random_int(min:number = -1000, max:number = 1000) : number {
    return Math.floor (min + Math.random()*(max-min+1));
}

function yes_no () : boolean {
    return random_int(0,1)==1;
}

function random_optional_int() : number|undefined {
    return yes_no() ? random_int() : undefined;
}

function random_float(min:number = -1e6, max:number = 1e6) : number {
    return random_int();
}

function random_optional_float() : number|undefined {
    return yes_no() ? random_float() : undefined;
}

function random_string(min:number = 0, max:number = 3) : string {
    let out: string = '';
    const input: string = 'abcdefghijklmnopqrstuvwxyz0123456789';
    for (let i = 0; i < 32; i++)
        out += input.charAt(random_int(0,input.length));
    return out;
}

function random_optional_string() : string|undefined {
    return yes_no() ? random_string() : undefined;
}

function random_list_of_ints (min:number = 0, max:number = 3) : number[] {
    const size = random_int(min,max);
    let list:number[] = [];
    for(let i=0; i<size; i++)
        list.push(random_int());
    return list;
}

function random_optional_list_of_ints() : number[]|undefined {
    return yes_no() ? random_list_of_ints() : undefined;
}

function random_list_of_floats (min:number = 0, max:number = 3) : number[] {
    const size = random_int(min,max);
    let list:number[] = [];
    for(let i=0; i<size; i++)
        list.push(random_float());
    return list;
}

function random_optional_list_of_floats() : number[]|undefined {
    return yes_no() ? random_list_of_floats() : undefined;
}

function random_list_of_strings (min:number = 0, max:number = 3) : string[] {
    const size = random_int(min,max);
    let list:string[] = [];
    for(let i=0; i<size; i++)
        list.push(random_string());
    return list;
}

function random_optional_list_of_strings() : string[]|undefined {
    return yes_no() ? random_list_of_strings() : undefined;
}

// https://stackoverflow.com/questions/1068834/object-comparison-in-javascript/6713782#6713782
function object_equals( x, y ) {
    if ( x === y ) return true;
      // if both x and y are null or undefined and exactly the same
  
    if ( ! ( x instanceof Object ) || ! ( y instanceof Object ) ) return false;
      // if they are not strictly equal, they both need to be Objects
  
    if ( x.constructor !== y.constructor ) return false;
      // they must have the exact same prototype chain, the closest we can do is
      // test there constructor.
  
    for ( var p in x ) {
      if ( ! x.hasOwnProperty( p ) ) continue;
        // other properties were tested using x.constructor === y.constructor
  
      if ( ! y.hasOwnProperty( p ) ) return false;
        // allows to compare x[ p ] and y[ p ] when set to undefined
  
      if ( x[ p ] === y[ p ] ) continue;
        // if they have the same strict value or identity then they are equal
  
      if ( typeof( x[ p ] ) !== "object" ) return false;
        // Numbers, Strings, Functions, Booleans must be strictly equal
  
      if ( ! object_equals( x[ p ],  y[ p ] ) ) return false;
        // Objects and Arrays must be tested recursively
    }
  
    for ( p in y )
      if ( y.hasOwnProperty( p ) && ! x.hasOwnProperty( p ) )
        return false;
          // allows x[ p ] to be set to undefined
  
    return true;
}

//create-struct-random//

function create (struct_name:string, file_name:string){
    if(false){
//create-struct-tests//
    } else
        throw new Error(`Cannot create an object of the structure ${struct_name}.`);
}

function convert (struct_name:string, file1_name:string, file2_name:string){
    if(false){
//convert-struct-tests//
    } else
        throw new Error(`Cannot convert an object of the structure ${struct_name}.`);
}

function compare (struct_name:string, file1_name:string, file2_name:string){
    if(false){
//compare-struct-tests//
    } else
        throw new Error(`Cannot compare an object of the structure ${struct_name}.`);
}

function main () {
    // expect at least 3 args
    if(process.argv.length<3)
        throw new Error(`Expect at least 3 args, found ${process.argv.length}`);

    var command = process.argv[2];

    if(command=='create'){
        if(process.argv.length<5)
            throw new Error(`Command "${command}" expects at least 5 args, found ${process.argv.length}`);
        create(process.argv[3],process.argv[4]);
    }
    else if(command=='convert'){
        if(process.argv.length<6)
            throw new Error(`Command "${command}" expects at least 6 args, found ${process.argv.length}`);
        convert(process.argv[3],process.argv[4],process.argv[5]);
    }
    else if(command=='compare'){
        if(process.argv.length<6)
            throw new Error(`Command "${command}" expects at least 6 args, found ${process.argv.length}`);
        compare(process.argv[3],process.argv[4],process.argv[5]);
    } else
        throw new Error(`Unknown command "${command}"`);
}

main();
'''