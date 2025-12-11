import os, math, logging
from .all import *
from .Code import *

logger = logging.getLogger(__name__)

class CodeCpp (Code):
    def __init__ (self, options={}):
        super().__init__('cpp','cpp',options)
        self.namespace = 'dto'
        self.header_extension = 'hpp'

    def TypeToString (self, var:Variable) -> str:

        m = {
            BasicType.null    : 'void',
            BasicType.string  : 'std::string',
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
            tname = f'std::map<{m.get(kv[0],kv[0])},{m.get(kv[1],kv[1])}>'

        type_str = m.get(tname,tname)

        if type(var)==Variable:
            if var.list:
                type_str = f'std::vector<{type_str}>'
            if var.optional:
                type_str = f'std::optional<{type_str}>'

        return type_str

    def ValueToString (self, arg) -> str:

        if arg is None:
            return '{}'
        elif isinstance(arg,Variable):
            return arg.name
        elif isinstance(arg,list):
            x = [ f'{item.name}'   for item in arg]
            y = ','.join(x)
            return f'{{{y}}}'
        elif isinstance(arg,str):
            return f'"{arg}"'
        elif isinstance(arg,bool):
            return f'{"true" if arg else "false"}'
        elif isinstance(arg,int):
            return f'{arg}'
        elif isinstance(arg,float):
            if math.isnan(arg):
                return 'NAN'
            else:
                return str(arg)
        else:
            raise Exception(f'Not supported: {arg}')

    def GeneratorDto (self, objs):
        ext_hpp = self.header_extension

        for obj in objs:
            if isinstance(obj,Struct):
                fname = f'{self.GetDirDto()}/{obj.name}.{ext_hpp}'
                yield (fname, '#pragma once')
                for line in self.GeneratorFilePrefix(objs):
                    yield (fname, line)
                for line in self.GeneratorStruct(obj):
                    yield (fname, line)
                yield (fname, '')

    def GeneratorTests (self, objs):
        fname = self.GetTestFileName()
        for line in self.GeneratorTest(objs):
            yield (fname, line)

    def GeneratorFilePrefix (self, objs):

        schema_version = self.options.get('schema_version')
        if schema_version:
            for line in autogen_text(schema_version).split('\n'):
                yield f'// {line}'

        for line in f'''

#include <optional>
//#include <variant>
#include <string>
#include <vector>
#include <map>
#include <stdexcept>
#include <cmath>

#include <nlohmann/json.hpp>
using json = nlohmann::json;

'''.split('\n'):
            yield line

    def GeneratorStruct (self, obj:Struct):

        for dep in obj.dependencies:
            yield f'#include "{dep.name}.{self.header_extension}"'

        yield f'namespace {self.namespace} {{'

        if obj.namespace:
            yield f'namespace {obj.namespace} {{'

        # Start with the forward declarations
        yield f'class {obj.name};'
        yield f'std::string {obj.name}_to_json_string(const {obj.name} &obj);'

        if obj.base:
            yield f'class {obj.name}: public {obj.base.name} {{'
        else:
            yield f'class {obj.name} {{'
        yield f'public:'
        yield f''

        for attr in obj.attributes:
            default_value = ''
            if attr.defval is not None:
                default_value = f' {{{self.ValueToString(attr.defval)}}}'
            if attr.doc:
                yield f'{indent}/**'
                yield f'{indent} * @brief {attr.doc}'
                yield f'{indent} */'
            yield f'{indent}{self.TypeToString(attr)} {attr.name}{default_value};'

        yield ''

        for func in obj.methods:
            if func.type=='constructor' or func.code.get(self.language):
                for line in self.GeneratorFunction(func,obj):
                    yield f'{indent}{line}'
                yield ''

        for line in self.GeneratorStructCompare(obj):
            yield line

        yield f'{indent*1}std::string json (void) const {{'
        yield f'{indent*2}return {obj.name}_to_json_string(*this);'
        yield f'{indent*1}}}'

        yield f'}}; // {obj.name}'

        for line in self.GeneratorStructToJson(obj):
            yield line
        for line in self.GeneratorStructToJsonString(obj):
            yield line
        for line in self.GeneratorStructFromJson(obj):
            yield line
        for line in self.GeneratorStructFromJsonString(obj):
            yield line

        if obj.namespace:
            yield f'}} // namespace {obj.namespace}'

        if obj.namespace and obj.default_version:
            yield f'using {obj.namespace}::{obj.name};'

        yield f'}} // namespace {self.namespace}'

    def GeneratorFunction (self, func:Function, base:Struct=None):
        if base and func.name==base.name:
            for item in self.GeneratorConstructor(func,base):
                yield item
        else:
            ftype = self.TypeToString(func.ReturnType()) + ' '
            if func.type==base and not func.const:
                ftype += '& '

            yield f'{ftype}{func.name} ('

            args_code = []
            for a in func.args:
                default = '' if a.defval is None else f' = {self.ValueToString(a.defval)}'
                args_code.append(f'{indent}{self.TypeToString(a)} {a.name}{default}')
            for i in range(len(args_code)-1):
                args_code[i] += ','
            for item in args_code:
                yield item
            if base and func.const:
                yield ') const'
            else:
                yield ')'

        yield '{'
        for line in get_code(func.code.get('cpp')):
            yield f'{indent}{line}'
        yield '}'

    def GeneratorConstructor(self, ctor:Function, base:Struct=None):
        assert ctor.name == base.name
        yield ''

        yield f'{ctor.name} ('
        for i,arg in enumerate(ctor.args):
            if arg.defval is not None:
                defval = f' = {self.ValueToString(arg.defval)}'
            elif arg.optional:
                defval = ' = {}'
            else:
                defval = ''
            yield f'{indent}{self.TypeToString(arg)} {arg.name}{defval}{"," if i+1<len(ctor.args) else ""}'
        yield ')'

        for i,(name,mapping) in enumerate(ctor.mapping):
            yield f'{":" if i==0 else ","} {name} ('
            for i,v in enumerate(mapping):
                line = self.ValueToString(v)
                yield indent + line + (',' if i+1<len(mapping) else '')
            yield ')'

    def GeneratorStructCompare(self, obj:Struct):
        yield f'{indent}bool operator == (const {obj.name} &other) const {{'
        if obj.base:
            yield f'{indent*2}if ({obj.base.name}::operator != (other)) return false;'
        for a in obj.attributes:
            if a.skip_dto: continue
            yield f'{indent*2}if ({a.name} != other.{a.name}) return false;'
        yield f'{indent*2}return true;'
        yield f'{indent}}}'
        yield f'{indent}bool operator != (const {obj.name} &other) const {{return not(*this==other);}}'

    def GeneratorStructToJson (self, obj:Struct):
        function_name = f'void to_json(json &j, const {obj.name} &obj)'
        yield 'inline'
        yield f'{function_name} try {{'
        yield f'{indent}j = json::object();'
        if obj.base:
            yield f'{indent}to_json(j,static_cast<const {obj.base.name} &>(obj));'
        for attr in obj.attributes:
            if attr.skip_dto: continue
            if attr.optional:
                yield f'{indent*1}if(obj.{attr.name}.has_value())'
                yield f'{indent*2}j["{attr.name}"] = obj.{attr.name}.value();'
            else:
                yield f'{indent}j["{attr.name}"] = obj.{attr.name};'
        yield f'}} catch (const std::exception &e) {{'
        yield f'{indent}std::throw_with_nested(std::runtime_error("{function_name} exception"));'
        yield f'}}'
        yield ''

    def GeneratorStructFromJson (self, obj:Struct):
        function_name = f'void from_json(const json &j, {obj.name} &obj)'
        yield 'inline'
        yield f'{function_name} try {{'
        if obj.base:
            yield f'{indent}from_json(j,static_cast<{obj.base.name} &>(obj));'
        for attr in obj.attributes:
            if attr.skip_dto: continue
            if attr.optional:
                yield f'{indent*1}if(auto it=j.find("{attr.name}"); it!=j.end() and !it->is_null())'
                yield f'{indent*2}obj.{attr.name} = *it;'
            else:
                yield f'{indent}j.at("{attr.name}").get_to(obj.{attr.name});'
        yield f'}} catch (const std::exception &e) {{'
        yield f'{indent}std::throw_with_nested(std::runtime_error("{function_name} exception"));'
        yield f'}}'

    def GeneratorStructToJsonString (self, obj:Struct):
        yield 'inline'
        yield f'std::string {obj.name}_to_json_string(const {obj.name} &obj) {{'
        yield f'{indent}json j;'
        yield f'{indent}to_json(j,obj);'
        yield f'{indent}return j.dump();'
        yield f'}}'

    def GeneratorStructFromJsonString (self, obj:Struct):
        yield 'inline'
        yield f'{obj.name} {obj.name}_from_json(const json &j) {{'
        yield f'{indent}{obj.name} obj;'
        yield f'{indent}from_json(j,obj);'
        yield f'{indent}return obj;'
        yield f'}}'
        return

    def GetTestFileName (self):
        return f'{self.GetDirTest()}/{self.name_test}.{self.extension}'

    def GeneratorTest (self, objs):

        code_include = []
        forward_declarations = []
        code_construct_random = []
        code_create = []
        code_convert = []
        code_compare = []

        for obj in objs:
            if not isinstance(obj,Struct):
                continue
            if not obj.gen_test:
                continue

            code_include.append(f'#include "{obj.name}.{self.header_extension}"')

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
                # elif arg.variant and not arg.list and not arg.optional:
                #     random_arg = f'random_variant_{arg.name}()'
                else:
                    raise Exception('Development error')
                ending = '' if (i+1)==len(ctors[0].args) else ','
                random_args += f'{indent*2}{random_arg}{ending}\n'

            if obj.namespace:
                forward_declarations.append(f'namespace {obj.namespace} {{')
            forward_declarations.append(f'// Forward declarations for {obj.name}')
            forward_declarations.append(f'class {obj.name};')
            forward_declarations.append(f'{obj.name} random_{obj.name} (void);')
            forward_declarations.append(f'std::optional<{obj.name}> random_optional_{obj.name} (void);')
            forward_declarations.append(f'std::vector<{obj.name}> random_list_{obj.name} (int min=0, int max=3);')
            forward_declarations.append(f'std::optional<std::vector<{obj.name}>> random_optional_list_{obj.name} (int min=0, int max=3);')
            forward_declarations.append(f'')
            if obj.namespace:
                forward_declarations.append(f'}} // namespace {obj.namespace}')

            if obj.namespace:
                code_construct_random.append(f'namespace {obj.namespace} {{')
            code_construct_random.extend(f'''
{obj.name} random_{obj.name} (void) {{
    return {obj.name} (
{random_args}
    );
}}
'''.split('\n'))

            code_construct_random.extend(f'''
std::optional<{obj.name}> random_optional_{obj.name} (void) {{
    if(random_boolean())
        return {{}};
    return random_{obj.name} ();
}}
'''.split('\n'))

            code_construct_random.extend(f'''
std::vector<{obj.name}> random_list_{obj.name} (int min, int max) {{
    std::vector<{obj.name}> list;
    if(recursionDepth<maxRecursionDepth) {{
        recursionDepth++;
        const auto size = random_int(min,max);
        for(int i=0; i<size; i++)
            list.push_back(random_{obj.name}());
        recursionDepth--;
    }}
    return list;
}}
'''.split('\n'))

            code_construct_random.extend(f'''
std::optional<std::vector<{obj.name}>> random_optional_list_{obj.name} (int min, int max) {{
    if(random_boolean())
        return {{}};
    return random_list_{obj.name} (min,max);
}}
'''.split('\n'))

            namespace = lambda: f'{self.namespace}::{obj.namespace}' if obj.namespace else f'{self.namespace}'

            code_create.append(f'''
        }} else if (struct_name == "{obj.name}") {{
            auto obj1 = {namespace()}::random_{obj.name}();
            std::ofstream(file1_path) << {namespace()}::{obj.name}_to_json_string(obj1);
            auto obj2 =
                {namespace()}::{obj.name}_from_json (
                    json::parse (
                        std::ifstream (
                            file1_path
            )));
            if(obj1!=obj2){{
                std::cerr << "obj1: " << {namespace()}::{obj.name}_to_json_string(obj1) << "\\n";
                std::cerr << "obj2: " << {namespace()}::{obj.name}_to_json_string(obj2) << "\\n";
                throw std::runtime_error("Operation 'compare' failed for struct " + struct_name);
            }}
''')

            code_convert.extend(f'''
        }} else if (struct_name == "{obj.name}") {{
            auto obj =
                {namespace()}::{obj.name}_from_json (
                    json::parse (
                        std::ifstream (
                            file1_path
            )));
            std::ofstream out (file2_path);
            out << {obj.name}_to_json_string(obj);
            if(!out)
                throw std::runtime_error("Operation 'convert': IO error on " + struct_name);
'''.split('\n'))
            code_compare.extend(f'''
        }} else if (struct_name == "{obj.name}") {{
            auto obj1 =
                {namespace()}::{obj.name}_from_json (
                    json::parse (
                        std::ifstream (
                            file1_path
            )));
            auto obj2 =
                {namespace()}::{obj.name}_from_json (
                    json::parse (
                        std::ifstream (
                            file2_path
            )));
            if(obj1!=obj2)
                throw std::runtime_error("Operation 'compare' failed for struct " + struct_name);
'''.split('\n'))

            if obj.namespace:
                code_construct_random.append(f'}} // namespace {obj.namespace}')
                if obj.default_version:
                    code_construct_random.append(f'')
                    code_construct_random.append(f'using {obj.namespace}::random_{obj.name};')
                    code_construct_random.append(f'using {obj.namespace}::random_list_{obj.name};')
                    code_construct_random.append(f'using {obj.namespace}::random_optional_{obj.name};')
                    code_construct_random.append(f'using {obj.namespace}::random_optional_list_{obj.name};')
                    code_construct_random.append(f'')

        cpp_test_template = '''
#include <optional>
#include <random>
#include <limits>
#include <filesystem>
#include <iostream>
#include <fstream>
#include <algorithm>

//include-dto//

namespace fs = std::filesystem;

//namespace-begin//

std::random_device rd;
std::mt19937 generator(rd());

unsigned recursionDepth {0};
constexpr unsigned maxRecursionDepth {5};

int random_int (
    int min = -1000,
    int max = 1000
) {
    std::uniform_int_distribution<int> uniform_dist(min,max);
    return uniform_dist (generator);
}

auto random_boolean = [] (void) -> bool {return random_int(0,1);};

std::optional<int> random_optional_int (
    int min = -1000,
    int max = 1000
) {
    if(random_boolean())
        return random_int(min,max);
    else
        return {};
}

std::vector<int> random_list_int (
    int len_min = 0,
    int len_max = 3,
    int int_min = -1000,
    int int_max = 1000
) {
    const auto size = random_int (len_min, len_max);
    std::vector<int> list;
    for(int i=0; i<size; i++)
        list.push_back(random_int(int_min,int_max));
    return list;
}

std::optional<std::vector<int>> random_optional_list_int (
    int len_min = 0,
    int len_max = 3,
    int int_min = -1000,
    int int_max = 1000
) {
    if(random_boolean())
        return random_list_int(len_min,len_max,int_min,int_max);
    else
        return {};
}

float random_float (
    float min            = -1e6,
    float max            =  1e6,
    bool can_be_nan      = false,
    bool can_be_infinity = false
) {
    // FIXME
    return (float) random_int(min,max);
#if 0
    if(can_be_nan and random_boolean())
        return NAN;

    if(can_be_infinity and random_boolean())
        return (random_boolean() ? -1 : 1) * std::numeric_limits<float>::infinity();

    std::uniform_real_distribution uniform_dist(min,max);
    return uniform_dist (generator);
#endif
}

std::optional<float> random_optional_float (
    float min            = -1e6,
    float max            =  1e6,
    bool can_be_nan      = false,
    bool can_be_infinity = false
) {
    if(random_boolean())
        return random_float(min,max,can_be_nan,can_be_infinity);
    else
        return {};
}

std::vector<float> random_list_float (
    int   len_min         = 0,
    int   len_max         = 3,
    float min             = -1e6,
    float max             =  1e6,
    bool  can_be_nan      = false,
    bool  can_be_infinity = false
) {
    const auto size = random_int (len_min, len_max);
    std::vector<float> list;
    for(int i=0; i<size; i++)
        list.push_back(random_float(min,max,can_be_nan,can_be_infinity));
    return list;
}

std::optional<std::vector<float>> random_optional_list_float (
    int   len_min         = 0,
    int   len_max         = 3,
    float min             = -1e6,
    float max             =  1e6,
    bool  can_be_nan      = false,
    bool  can_be_infinity = false
) {
    if(random_boolean())
        return random_list_float(len_min,len_max,min,max,can_be_nan,can_be_infinity);
    else
        return {};
}

// https://stackoverflow.com/questions/47977829/generate-a-random-string-in-c11
std::string random_string (int len_min=0, int len_max=2) {
    static std::string str("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz");
    std::shuffle(str.begin(), str.end(), generator);
    return str.substr(0, random_int (len_min, len_max));
}

std::optional<std::string> random_optional_string (int len_min=0, int len_max=2) {
    if(random_boolean())
        return random_string(random_int (len_min, len_max));
    else
        return {};
}

std::vector<std::string> random_list_string (
    int len_min = 0,
    int len_max = 3,
    int strlen_min = 0,
    int strlen_max = 2
) {
    const auto size = random_int (len_min, len_max);
    std::vector<std::string> list;
    for(int i=0; i<size; i++)
        list.push_back(random_string(strlen_min,strlen_max));
    return list;
}

std::optional<std::vector<std::string>> random_optional_list_string (
    int len_min = 0,
    int len_max = 3,
    int strlen_max = 16
) {
    if(random_boolean())
        return random_list_string(len_min,len_max,strlen_max);
    else
        return {};
}

//forward-declarations//

//create-struct-random//

//namespace-end//

int main (int argc, const char **argv) try {

    const std::string
        command         = argc>1 ? argv[1] : "",
        struct_name     = argc>2 ? argv[2] : "",
        file1_path      = argc>3 ? argv[3] : "",
        file2_path      = argc>4 ? argv[4] : "";

    if (command == "create") {

        if(!file2_path.empty())
            throw std::runtime_error("Command 'create' expects empty file2 name, got:'" + file2_path + '"');

        std::ofstream f (file1_path);

        if (false) {
//create-struct-tests//
        } else {
            throw std::runtime_error("Not supported operation 'create' on struct " + struct_name);
        }
        if(!f)
            throw std::runtime_error("Operation 'create': IO error");

    } else if (command == "convert") {

        if (false) {
//convert-struct-tests//
        } else {
            throw std::runtime_error("Not supported operation 'convert' on struct " + struct_name);
        }

    } else if (command == "compare") {

        if (false) {
//compare-struct-tests//
        } else {
            throw std::runtime_error("Not supported operation 'compare' on struct " + struct_name);
        }

    } else {
        throw std::runtime_error("Not supported command " + command);
    }

    return 0;

} catch (const std::exception &e) {
    std::cerr << "Exception:" << std::endl << e.what() << std::endl;
    return 1;
}

catch (...) {
    std::cerr << "Unknown exception:" << std::endl;
    return 1;
}
'''

        for line in cpp_test_template.split('\n'):
            if line=='//namespace-begin//':
                yield f'namespace {self.namespace} {{'
            elif line=='//namespace-end//':
                yield f'}} // namespace {self.namespace}'
            elif line=='//include-dto//':
                for line in code_include:
                    yield line

            elif line=='//forward-declarations//':
                for line in forward_declarations:
                    yield line
            elif line=='//create-struct-random//':
                for line in code_construct_random:
                    yield line
            elif line=='//create-struct-tests//':
                for line in code_create:
                    yield line
            elif line=='//convert-struct-tests//':
                for line in code_convert:
                    yield line
            elif line=='//compare-struct-tests//':
                for line in code_compare:
                    yield line
            else:
                yield line

    def CreateTestEnv(self, objs):

        os.makedirs (self.GetDirTestEnv(), exist_ok=True)

        abs_test_source = os.path.abspath(self.GetTestFileName())
        abs_include_dir = os.path.abspath(self.GetDirDto())

        meson_build = f'''
project (
        'cpp',
        ['cpp'],
        default_options : [
                'cpp_std=c++20',
                'buildtype=release',
        ]
)

add_global_arguments('-Wno-narrowing', language : 'cpp')

executable (
    'test-cpp',
    sources: ['{abs_test_source}'],
    include_directories : ['{abs_include_dir}'],
    link_with    : [],
    dependencies : []
)
'''

        run = f'''#!/usr/bin/env bash

case "$1" in
    build)
        if [ ! -f nlohmann/json.hpp ]; then
            mkdir nlohmann
            (cd nlohmann; wget https://github.com/nlohmann/json/releases/download/v3.11.2/json.hpp)
        fi
        meson setup build
        cd build
        ninja
        ;;
    *)
        cd build
        ./test-cpp $@
        ;;
esac
'''

        with open(f'{self.GetDirTestEnv()}/meson.build','w') as f:
            f.write(meson_build)

        name = f'{self.GetDirTestEnv()}/run'
        with open(name,'w') as f:
            f.write(run)
        os.chmod(name,0o777)

        logger.info(f'Building "{self.language}" test environment...')
        run_test(self.GetDirTestEnv(),'build')

        self.test_environment_ready = True

register(CodeCpp)
