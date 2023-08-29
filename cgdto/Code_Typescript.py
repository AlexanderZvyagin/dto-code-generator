import os, math
from .all import *
from .Code import *

class CodeTypescript (Code):
    def __init__ (self, options={}):
        super().__init__('typescript','ts',options)

    def TypeToString (self, var:Variable) -> str:

        m = {
            'void'    : 'void',
            'string'  : 'string',
            'boolean' : 'boolean',
            'int'     : 'number',
            'float'   : 'number',
        }

        tname = var.TypeName()

        kv = detect_dict_key_value(tname)
        if kv:
            tname = f'{{[key:{m.get(kv[0],kv[0])}]: {m.get(kv[1],kv[1])}}}'

        type_str = m.get(tname,tname)

        if var.list:
            type_str = f'{type_str}[]'
        if var.optional:
            type_str = f'{type_str}|undefined'
        return type_str

    def ValueToString (self, arg) -> str:
        if arg is None:
            return 'undefined'
        elif isinstance(arg,Variable):
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
                yield f'// {line}'

        for line in '''
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

'''.split('\n'): yield line

    def GeneratorSingleDtoFileSuffix (self, objs):
        yield 'export {'
        for obj in objs:
            if isinstance(obj,Struct) or isinstance(obj,Function):
                yield f'{indent}{obj.name},'
        yield '}'

    def GeneratorSingleDtoFileBody (self, objs):
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
            elif isinstance(obj,Include):
                separation_line = '//'*32
                for file in obj.files.get(self.language,[]):
                    yield separation_line
                    yield f'// The start of "{file}"'
                    yield separation_line
                    for line in open(file).readlines():
                        yield line.rstrip('\n')
                    yield separation_line
                    yield f'// The end of "{file}"'
                    yield separation_line
                yield ''
            else:
                print(f'Cannot handle {type(obj)}')

    def GeneratorStruct (self, obj:Struct):
        if obj.base:
            yield f'class {obj.name} extends {obj.base.name} {{'
        else:
            yield f'class {obj.name} {{'
        yield f''

        for attr in obj.attributes:
            if attr.static:
                assert attr.defval is not None
                yield f'{indent}static {attr.name} : {self.TypeToString(attr)} = {self.ValueToString(attr.defval)};'

        for a in obj.attributes:
            if a.static: continue
            yield f'{indent}{a.name} : {self.TypeToString(a)};'

        yield ''

        for func in obj.methods:
            if func.code and func.code.get('typescript','') is None: continue
            for line in self.GeneratorFunction(func,obj):
                yield f'{indent}{line}'
            yield ''

        yield f'{indent*1}json (): string {{'
        yield f'{indent*2}return {obj.name}_to_json_string(this);'
        yield f'{indent*1}}}'

        yield f'}}'

        for line in self.GeneratorStructCompare(obj):
            yield line

        for line in self.Generator2StructFromJsonString(obj):
            yield line
        for line in self.GeneratorStructFromJsonString(obj):
            yield line
        for line in self.GeneratorStructToJsonString(obj):
            yield line
        for line in self.GeneratorStructFromJson(obj):
            yield line
        for line in self.GeneratorStructToJson(obj):
            yield line

    def GeneratorFunction (self, func:Function, obj:Struct=None):
        if obj and func.name==obj.name:
            for line in self.GeneratorConstructor(func,obj):
                yield line
        else:
            ftype = self.TypeToString(Variable('',func.type))+' '

            yield f'{func.name} ('

            for a in func.args:
                yield f'{indent}'
                default = '' if a.defval is None else f' = {self.ValueToString(a.defval)}'
                yield f'{indent}{a.name} : {self.TypeToString(a)}{default},'
            yield f') : {ftype} {{'

        for line in get_code(func.code.get('typescript')):
            yield f'{indent}{line}'
        yield '}'

    def GeneratorConstructor(self, ctor:Function, base:Struct=None):
        yield f'constructor('

        for arg in ctor.args:
            if arg.defval is not None:
                if isinstance(arg.defval,Variable) and isinstance(arg.defval.type,Struct):
                    defval = f' = new {self.ValueToString(arg.defval)}'
                else:
                    defval = f' = {self.ValueToString(arg.defval)}'
            elif arg.optional:
                defval = ' = undefined'
            else:
                defval = ''
            yield f'{indent}{arg.name} : {self.TypeToString(arg)} {defval},'
        yield '){'

        for name,mapping in ctor.mapping:
            if base.base and base.base.name == name:
                yield f'{indent}super('
                for v in mapping:
                    yield f'{indent*2}{self.ValueToString(v)},'
                yield f'{indent});'
            else:
                assert len(mapping)==1
                yield f'{indent}this.{name} = {self.ValueToString(mapping[0])};'

        yield f''

    def GeneratorStructCompare(self, obj:Struct):
        yield f'export function'
        yield f'{obj.name}_equal (a: {obj.name}, b: {obj.name}) : boolean {{'
        if obj.base:
            yield f'{indent}if(!{obj.base.name}_equal(a,b)) return false;'
        for attr in obj.attributes:
            if attr.skip_dto: continue
            lvl=1
            if attr.optional:
                yield f'{indent*1}if(a.{attr.name}===undefined && b.{attr.name}!==undefined) return false;'
                yield f'{indent*1}if(a.{attr.name}!==undefined && b.{attr.name}===undefined) return false;'
                yield f'{indent*1}if(a.{attr.name}!==undefined && b.{attr.name}!==undefined)'
                if attr.list:
                    yield f'{indent*2}if(!list_equal(a.{attr.name}!,b.{attr.name}!,{attr.TypeName()}_equal)) return false;'
                else:
                    yield f'{indent*lvl}if(!{attr.TypeName()}_equal(a.{attr.name}!,b.{attr.name}!)) return false;'
            elif attr.list:
                yield f'{indent*1}if(!list_equal(a.{attr.name},b.{attr.name},{attr.TypeName()}_equal)) return false;'
            else:
                yield f'{indent*lvl}if(!{attr.TypeName()}_equal(a.{attr.name},b.{attr.name})) return false;'
        yield f'{indent*1}return true;'
        yield f'}}'
        yield f''

    def GeneratorStructFromJson (self, obj:Struct):
        yield f'export function'
        yield f'{obj.name}_from_json(j:object, obj:{obj.name}) {{'
        if obj.base:
            yield f'{indent}{obj.base.name}_from_json(j,obj);'

        for attr in obj.attributes:
            if attr.skip_dto: continue
            if isinstance(attr.type,Struct):
                if attr.optional:
                    yield f'{indent*1}if( "{attr.name}" in j)'
                    yield f'{indent*2}obj.{attr.name} = j["{attr.name}"] as {self.TypeToString(attr)};'
                elif not attr.optional and attr.list:
                    yield f'{indent*1}for(let item of j["{attr.name}"]) {{'
                    yield f'{indent*2}const v: {attr.TypeName()} = new {attr.TypeName()}();'
                    yield f'{indent*2}{attr.TypeName()}_from_json(item,v);'
                    yield f'{indent*2}obj.{attr.name}.push(v);'
                    yield f'{indent*1}}}'
                else:
                    yield f'{indent}{attr.TypeName()}_from_json(j["{attr.name}"],obj.{attr.name});'
            else:
                if attr.optional:
                    yield f'{indent*1}if("{attr.name}" in j)'
                    yield f'{indent*2}obj.{attr.name} = j["{attr.name}"] as {self.TypeToString(attr)};'
                    yield f'{indent*1}else'
                    yield f'{indent*2}obj.{attr.name} = undefined;'
                else:
                    yield f'{indent}obj.{attr.name} = j["{attr.name}"];'

        yield f'}}'
        yield f''

    def GeneratorStructFromJsonString (self, obj:Struct):
        yield f'export function'
        yield f'{obj.name}_from_json_string (jstr:string): {obj.name} {{'
        yield f'{indent}const j: object = JSON.parse(jstr);'
        yield f'{indent}const obj: {obj.name} = new {obj.name}();'
        yield f'{indent}{obj.name}_from_json(j,obj);'
        yield f'{indent}return obj;'
        yield f'}}'
        yield f''

    def GeneratorStructToJson (self, obj:Struct):
        yield f'export function'
        yield f'{obj.name}_to_json(j:object, obj:{obj.name}) {{'
        if obj.base:
            yield f'{indent}{obj.base.name}_to_json(j,obj);'

        for attr in obj.attributes:
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
                yield f'{indent*1}if( obj.{attr.name} !== undefined) {{'
                for line in var_code:
                    yield f'{indent*2}{line}'
                yield f'{indent*1}}}'
            else:
                for line in var_code:
                    yield f'{indent*1}{line}'

        yield f'}}'
        yield f''

    def GeneratorStructToJsonString (self, obj:Struct):
        yield f'export function'
        yield f'{obj.name}_to_json_string (self:{obj.name}) {{'
        yield f'{indent}const j = {{}};'
        yield f'{indent}{obj.name}_to_json(j,self);'
        yield f'{indent}return JSON.stringify(j);'
        yield f'}}'
        yield f''
    
    def Generator2StructFromJsonString (self, obj:Struct):
        yield f'export function'
        yield f'{obj.name}_fromJSON (j:any, obj: {obj.name}): void {{'
        if obj.base:
            yield f'{indent}{obj.base.name}_fromJSON(j,obj)'
        for attr in obj.attributes:
            if attr.skip_dto: continue
            if attr.optional:
                yield f'{indent*1}if("{attr.name}" in j)'
                yield f'{indent*2}obj.{attr.name} = j["{attr.name}"];'
            else:
                yield f'{indent*1}obj.{attr.name} = j["{attr.name}"];'
        yield '}'

        yield f'export function'
        yield f'{obj.name}_fromJSON_string (jstr:string): {obj.name} {{'
        yield f'{indent}const j = JSON.parse(jstr);'
        yield f'{indent}const obj = new {obj.name}();'
        yield f'{indent}{obj.name}_fromJSON(j,obj);'
        yield f'{indent}return obj;'
        yield f'}}'

###############################################

    def GeneratorTest (self, objs):

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
function random_{obj.name} () : {obj.name} {{
    return new {obj.name} (
{random_args}
    );
}}
'''.split('\n'))

            code_construct_random.extend(f'''
function random_optional_{obj.name} () : {obj.name}|undefined {{
    if(yes_no())
        return undefined;
    return random_{obj.name} ();
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

            code_construct_random.extend(f'''
function random_optional_list_{obj.name} () : {obj.name}[]|undefined {{
    if(yes_no())
        return undefined;
    return random_list_{obj.name} ();
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

        for line in typescript_test_template.split('\n'):
            if line=='//structs//':
                for l in [f'{indent}{name},' for name in struct_names]:
                    yield l
            elif line=='//create-struct-random//':
                for l in code_construct_random:
                    yield l
            elif line=='//create-struct-tests//':
                for l in code_create:
                    yield l
            elif line=='//convert-struct-tests//':
                for l in code_convert:
                    yield l
            elif line=='//compare-struct-tests//':
                for l in code_compare:
                    yield l
            else:
                yield line

    def CreateTestEnv(self, objs):

        os.makedirs (self.GetDirTestEnv(), exist_ok=True)

        ext_py = self.extension
        name = f'{self.name_dto}.{ext_py}'
        # os.symlink(f'../../{self.name_dto}/{self.language}/{name}',f'{self.GetDirTest()}/{name}')
        os.symlink(f'../../{self.name_dto}/{self.language}/{name}',f'{self.GetDirTestEnv()}/{name}')
        name = f'{self.name_test}.{ext_py}'
        os.symlink(f'../../{self.name_test}/{self.language}/{name}',f'{self.GetDirTestEnv()}/{name}')

        run = f'''#!/usr/bin/env bash

    case "$1" in
        build)
            npm install --save-dev typescript
            npm install --save-dev @types/node
            npm install --save-dev node-fetch@2.6.6
            ./node_modules/.bin/tsc {self.name_test}.{self.extension}
            ;;
        *)
            node {self.name_test}.js $@
            ;;
    esac
    '''

        name = f'{self.GetDirTestEnv()}/run'
        with open(name,'w') as f:
            f.write(run)
        os.chmod(name,0o777)

        print(f'Building "{self.language}" test environment...')
        run_test(self.GetDirTestEnv(),'build')

        self.test_environment_ready = True

register(CodeTypescript)
