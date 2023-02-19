from .all import *
import math

def typescript_type_to_string (var:Variable):

    tname = var.TypeName()

    type_str = {
        'void'    : 'void',
        'string'  : 'string',
        'boolean' : 'boolean',
        'int'     : 'number',
        'float'   : 'number',
    } .get(tname,tname)

    if var.list:
        type_str = f'{type_str}[]'
    if var.optional:
        type_str = f'{type_str}|undefined'
    return type_str

def typescript_value_to_string (arg):
    if isinstance(arg,Variable):
        return arg.name
    elif isinstance(arg,list):
        x = [ f'{item.name}'   for item in arg]
        y = ','.join(x)
        return f'[{y}]'
    elif isinstance(arg,str):
        return f'"{arg}"'
    elif isinstance(arg,float):
        if math.isnan(arg):
            return 'Number.NaN'
        else:
            return str(arg)
    else:
        return str(arg)

def File_prefix_typescript (objs):
    code = [f'// {autogen_text}']
    code.extend('''

function list_equal<Type> (
    a:Type[],
    b:Type[],
    eq:(a:Type,b:Type)=>boolean
): boolean {
    if(a.length!==b.length)
        return false;
    for(let i=0; i<a.length; i++)
        if(!eq(a[i],b[i]))
            return false;
    return true;
}

function float_equal (a:number, b:number) : boolean {
    if(Number.isNaN(a) && Number.isNaN(b)) return true;
    return a===b;
}

function int_equal (a:number, b:number) : boolean {
    return a===b;
}

function string_equal (a:string, b:string) : boolean {
    return a===b;
}

'''.split('\n'))
    return code


def File_suffix_typescript (objs):
    code = []
    code.append('export {')
    for obj in objs:
        if isinstance(obj,Struct) or isinstance(obj,Function):
            code.append(f'{indent}{obj.name},')
    code.append('}')
    return code

def Constructor_typescript(ctor:Function,base:Struct):
    code = []
    code.append(f'constructor(')

    for arg in ctor.args:
        if arg.defval is not None:
            code.append(f'{indent}// defval: {arg.defval}')
            if isinstance(arg.defval,Variable) and isinstance(arg.defval.type,Struct):
                defval = f' = new {typescript_value_to_string(arg.defval)}'
            else:
                defval = f' = {typescript_value_to_string(arg.defval)}'
        elif arg.optional:
            defval = ' = undefined'
        else:
            defval = ''
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
    code.extend(Struct_equal_typescript(self))
    code.extend(Struct_fromJSON_string_typescript(self))

    code.extend(Struct_to_json_typescript(self))
    code.extend(Struct_from_json_typescript(self))

    code.extend(Struct_to_json_string_typescript(self))
    code.extend(Struct_from_json_string_typescript(self))

    return code

def Struct_equal_typescript(self:Struct):
    code = []
    code.append(f'export function')
    code.append(f'{self.name}_equal (a: {self.name}, b: {self.name}) : boolean {{')
    if self.base:
        code.append(f'{indent}if(!{self.base.name}_equal(a,b)) return false;')
    for attr in self.attributes:
        lvl=1
        if attr.optional:
            code.append(f'{indent*1}if(a.{attr.name}===undefined && b.{attr.name}!==undefined) return false;')
            code.append(f'{indent*1}if(a.{attr.name}!==undefined && b.{attr.name}===undefined) return false;')
            code.append(f'{indent*1}if(a.{attr.name}!==undefined && b.{attr.name}!==undefined)')
            if attr.list:
                code.append(f'{indent*2}if(!list_equal(a.{attr.name}!,b.{attr.name}!,{attr.TypeName()}_equal)) return false;')
            else:
                code.append(f'{indent*lvl}if(!{attr.TypeName()}_equal(a.{attr.name}!,b.{attr.name}!)) return false;')
        elif attr.list:
            code.append(f'{indent*1}if(!list_equal(a.{attr.name},b.{attr.name},{attr.TypeName()}_equal)) return false;')
        else:
            code.append(f'{indent*lvl}// ')
            code.append(f'{indent*lvl}if(!{attr.TypeName()}_equal(a.{attr.name},b.{attr.name})) return false;')
    code.append(f'{indent*1}return true;')
    code.append(f'}}')
    code.append(f'')
    return code

def Struct_to_json_string_typescript (self:Struct) -> list[str]:
    code = []
    code.append(f'export function')
    code.append(f'{self.name}_to_json_string (self:{self.name}) {{')
    code.append(f'{indent}const j = {{}};')
    code.append(f'{indent}{self.name}_to_json(j,self);')
    code.append(f'{indent}return JSON.stringify(j);')
    code.append(f'}}')
    code.append(f'')
    return code

def Struct_from_json_string_typescript (self) -> list[str]:
    code = []
    code.append(f'export function')
    code.append(f'{self.name}_from_json_string (jstr:string): {self.name} {{')
    code.append(f'{indent}const j: object = JSON.parse(jstr);')
    code.append(f'{indent}const obj: {self.name} = new {self.name}();')
    code.append(f'{indent}{self.name}_from_json(j,obj);')
    code.append(f'{indent}return obj;')
    code.append(f'}}')
    code.append(f'')
    return code

def Struct_to_json_typescript (self:Struct):
    code = []
    code.append(f'export function')
    code.append(f'{self.name}_to_json(j:object, obj:{self.name}) {{')
    if self.base:
        code.append(f'{indent}{self.base.name}_to_json(j,obj);')

    for attr in self.attributes:
        if attr.skip_dto: continue
        var_code = []
        if isinstance(attr.type,str):
            var_code.append(f'j["{attr.name}"] = obj.{attr.name};')
        elif isinstance(attr.type,Struct) and not attr.list:
            var_code.append(f'{{')
            var_code.append(f'{indent}const jj = {{}};')
            var_code.append(f'{indent}{attr.TypeName()}_to_json(jj,obj.{attr.name});')
            var_code.append(f'{indent}j["{attr.name}"] = jj;')
            var_code.append(f'}}')
        elif isinstance(attr.type,Struct) and attr.list:
            var_code.append(f'j["{attr.name}"] = [];')
            var_code.append(f'for(let item of obj.{attr.name}) {{')
            var_code.append(f'{indent}const jj = {{}};')
            var_code.append(f'{indent}{attr.TypeName()}_to_json(jj,item);')
            var_code.append(f'{indent}j["{attr.name}"].push(jj);')
            var_code.append(f'}}')
        else:
            raise NotImplementedError()
        if attr.optional:
            code.append(f'{indent*1}if( obj.{attr.name} !== undefined) {{')
            for line in var_code:
                code.append(f'{indent*2}{line}')
            code.append(f'{indent*1}}}')
        else:
            for line in var_code:
                code.append(f'{indent*1}{line}')

    code.append(f'}}')
    code.append(f'')
    return code

def Struct_from_json_typescript (self:Struct):
    code = []
    code.append(f'export function')
    code.append(f'{self.name}_from_json(j:object, obj:{self.name}) {{')
    if self.base:
        code.append(f'{indent}{self.base.name}_from_json(j,obj);')

    for attr in self.attributes:
        if attr.skip_dto: continue
        if isinstance(attr.type,Struct):
            if attr.optional:
                code.append(f'{indent*1}if( "{attr.name}" in j)')
                code.append(f'{indent*2}obj.{attr.name} = j["{attr.name}"] as {typescript_type_to_string(attr)};')
            elif not attr.optional and attr.list:
                code.append(f'{indent*1}for(let item of j["{attr.name}"]) {{')
                code.append(f'{indent*2}const v: {attr.TypeName()} = new {attr.TypeName()}();')
                code.append(f'{indent*2}{attr.TypeName()}_from_json(item,v);')
                code.append(f'{indent*2}obj.{attr.name}.push(v);')
                code.append(f'{indent*1}}}')
            else:
                code.append(f'{indent}{attr.TypeName()}_from_json(j["{attr.name}"],obj.{attr.name});')
        else:
            if attr.optional:
                code.append(f'{indent*1}if("{attr.name}" in j)')
                code.append(f'{indent*2}obj.{attr.name} = j["{attr.name}"] as {typescript_type_to_string(attr)};')
                code.append(f'{indent*1}else')
                code.append(f'{indent*2}obj.{attr.name} = undefined;')
            else:
                code.append(f'{indent}obj.{attr.name} = j["{attr.name}"]')

    code.append(f'}}')
    code.append(f'')
    return code


def old_Struct_to_json_string_typescript (self:Struct):
    code = []
    code.append(f'{indent*1}toJSON () : object {{')
    if self.base is None:
        code.append(f'{indent*2}const obj = {{}};')
    else:
        code.append(f'{indent*2}const obj = super.toJSON();')
    for attr in self.attributes:
        if attr.skip_dto: continue
        if attr.optional:
            code.append(f'{indent*2}if(this.{attr.name}!==undefined)')
            code.append(f'{indent*3}obj["{attr.name}"] = this.{attr.name};')
        else:
            code.append(f'{indent*2}obj["{attr.name}"] = this.{attr.name};')
    code.append(f'{indent*2}return obj;')
    code.append(f'{indent*1}}}')
    return code

def Struct_fromJSON_string_typescript (self:Struct):
    code = []

    code.append(f'export function')
    code.append(f'{self.name}_fromJSON (j:any, obj: {self.name}): void {{')
    if self.base:
        code.append(f'{indent}{self.base.name}_fromJSON(j,obj)')
    for attr in self.attributes:
        if attr.skip_dto: continue
        if attr.optional:
            code.append(f'{indent*1}if("{attr.name}" in j)')
            code.append(f'{indent*2}obj.{attr.name} = j["{attr.name}"];')
        else:
            code.append(f'{indent*1}obj.{attr.name} = j["{attr.name}"];')
    code.append('}')

    code.append(f'export function')
    code.append(f'{self.name}_fromJSON_string (jstr:string): {self.name} {{')
    code.append(f'{indent}const j = JSON.parse(jstr);')
    code.append(f'{indent}const obj = new {self.name}();')
    code.append(f'{indent}{self.name}_fromJSON(j,obj);')
    code.append(f'{indent}return obj;')
    code.append(f'}}')
    return code

def Tests_typescript (objs):

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
function random_{obj.name} () : {obj.name} {{
    return new {obj.name} (
{random_args}
    );
}}
'''.split('\n'))

        code_construct_random.extend(f'''
function random_list_{obj.name} (min:number = 0, max:number = 3) : {obj.name}[] {{
    const size:number = Math.floor(min + Math.random()*(max-min));
    const list:{obj.name}[] = [];
    for(let i=0; i<size; i++)
        list.push(random_{obj.name}());
    return list;
}}
'''.split('\n'))

        code_create.append(f'''
    }} else if (struct_name === '{obj.name}') {{
        const obj1: {obj.name} = random_{obj.name}();
        const j: object = {{}};
        dto.{obj.name}_to_json(j,obj1);

        fs.writeFileSync (file_name, JSON.stringify (j));
        const obj2: {obj.name} = new {obj.name}();
        dto.{obj.name}_from_json(j,obj2);
        if(!dto.{obj.name}_equal(obj1,obj2))
            throw new Error(`${{struct_name}} objects are not equal.`);
''')

        code_convert.extend(f'''
    }} else if (struct_name === '{obj.name}') {{
        const jstr: string = fs.readFileSync(file1_name,'utf-8');
        const obj: {obj.name} = dto.{obj.name}_fromJSON_string(jstr);
        fs.writeFileSync(file2_name, JSON.stringify(obj));
'''.split('\n'))
        code_compare.extend(f'''
    }} else if (struct_name === '{obj.name}') {{
        const jstr1: string = fs.readFileSync(file1_name,'utf-8');
        const jstr2: string = fs.readFileSync(file2_name,'utf-8');
        const obj1: {obj.name} = dto.{obj.name}_fromJSON_string(jstr1);
        const obj2: {obj.name} = dto.{obj.name}_fromJSON_string(jstr2);
        if(!dto.{obj.name}_equal(obj1,obj2))
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

import * as dto from './dto'
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

function random_list_int (min:number = 0, max:number = 3) : number[] {
    const size = random_int(min,max);
    let list:number[] = [];
    for(let i=0; i<size; i++)
        list.push(random_int());
    return list;
}

function random_optional_list_int() : number[]|undefined {
    return yes_no() ? random_list_int() : undefined;
}

function random_list_float (min:number = 0, max:number = 3) : number[] {
    const size = random_int(min,max);
    let list:number[] = [];
    for(let i=0; i<size; i++)
        list.push(random_float());
    return list;
}

function random_optional_list_float() : number[]|undefined {
    return yes_no() ? random_list_float() : undefined;
}

function random_list_string (min:number = 0, max:number = 3) : string[] {
    const size = random_int(min,max);
    let list:string[] = [];
    for(let i=0; i<size; i++)
        list.push(random_string());
    return list;
}

function random_optional_list_string() : string[]|undefined {
    return yes_no() ? random_list_string() : undefined;
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