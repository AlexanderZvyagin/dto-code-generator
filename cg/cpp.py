from .all import *
import math

def cpp_type_to_string (var:Variable):

    tname = var.TypeName()

    type_str = {
        'void'    : 'void',
        'string'  : 'std::string',
        'boolean' : 'bool',
        'int'     : 'int',
        'float'   : 'float',
    } .get(tname,tname)

    if var.list:
        type_str = f'std::vector<{type_str}>'
    if var.optional:
        type_str = f'std::optional<{type_str}>'
    return type_str

def cpp_value_to_string (arg):
    if isinstance(arg,Variable):
        return arg.name
    elif isinstance(arg,list):
        x = [ f'{item.name}'   for item in arg]
        y = ','.join(x)
        return f'{{{y}}}'
    elif isinstance(arg,str):
        return f'"{arg}"'
    elif isinstance(arg,float):
        if math.isnan(arg):
            return 'NAN'
        else:
            return str(arg)
    else:
        return str(arg)

def Constructor_cpp(ctor:Function,base:Struct):
    assert ctor.name == base.name
    code = []
    code.append('')
    
    code.append(f'{ctor.name} (')
    for i,arg in enumerate(ctor.args):
        if arg.defval is not None:
            defval = f' = {cpp_value_to_string(arg.defval)}'
        elif arg.optional:
            defval = ' = {}'
        else:
            defval = ''
        code.append(f'{indent}{cpp_type_to_string(arg)} {arg.name}{defval}{"," if i+1<len(ctor.args) else ""}')
    code.append(f')')

    for i,(name,mapping) in enumerate(ctor.mapping):
        code.append(f'{":" if i==0 else ","} {name} (')
        for i,v in enumerate(mapping):
            line = cpp_value_to_string(v)
            code.append(indent + line + (',' if i+1<len(mapping) else ''))
        code.append(')')

    return code

def Function_cpp(self:Function, obj:Struct=None):

    code = []

    if obj and self.name==obj.name:
        code = Constructor_cpp(self,obj)
    else:
        ftype = cpp_type_to_string(Variable('',self.type))+' '

        code = []
        code.append(f'{ftype}{self.name} (')

        args_code = []
        for a in self.args:
            default = '' if a.defval is None else f' = {cpp_value_to_string(a.defval)}'
            args_code.append(f'{indent}{cpp_type_to_string(a)} {a.name}{default}')
        for i in range(len(args_code)-1):
            args_code[i] += ','
        code.extend(args_code)
        if obj and self.const:
            code.append(') const')
        else:
            code.append(')')

    code.append('{')
    for line in get_code(self.code.get('cpp')):
        code.append(f'{indent}{line}')
    code.append('}')

    return code

def Struct_cpp (self:Struct):
    code = []
    if self.base:
        code.append(f'class {self.name}: public {self.base.name} {{')
    else:
        code.append(f'class {self.name} {{')
    code.append(f'public:')
    code.append(f'')
    
    for a in self.attributes:
        code.append(f'{indent}{cpp_type_to_string(a)} {a.name};')

    code.append('')

    for func in self.methods:
        for line in Function_cpp(func,self):
            code.append(f'{indent}{line}')
        code.append('')

    code.extend(Struct_compare_cpp(self))

    code.append(f'}};')

    code.extend(Struct_to_JSON_cpp(self))
    code.extend(Struct_to_JSON_string_cpp(self))
    code.extend(Struct_from_JSON_cpp(self))
    code.extend(Struct_from_JSON_string_cpp(self))

    return code

def Struct_compare_cpp(self:Struct):
    code = []
    code.append(f'{indent}bool operator == (const {self.name} &other) const {{')
    if self.base:
        code.append(f'{indent*2}if ({self.base.name}::operator != (other)) return false;')
    for a in self.attributes:
        code.append(f'{indent*2}if ({a.name} != other.{a.name}) return false;')
    code.append(f'{indent*2}return true;')
    code.append(f'{indent}}}')
    code.append(f'{indent}bool operator != (const {self.name} &other) const {{return not(*this==other);}}')
    return code

def Struct_to_JSON_cpp (self:Struct):
    code = []
    code.append(f'void to_json(json &j, const {self.name} &obj) {{')
    if self.base:
        code.append(f'{indent}to_json(j,static_cast<const {self.base.name} &>(obj));')
    for attr in self.attributes:
        if attr.skip_dto: continue
        if attr.optional:
            code.append(f'{indent*1}if(obj.{attr.name}.has_value())')
            code.append(f'{indent*2}j["{attr.name}"] = obj.{attr.name}.value();')
        else:
            code.append(f'{indent}j["{attr.name}"] = obj.{attr.name};')
    code.append(f'}}')
    code.append('')
    return code

def Struct_from_JSON_cpp (self:Struct):
    code = []
    code.append(f'void from_json(const json &j, {self.name} &obj) {{')
    if self.base:
        code.append(f'{indent}from_json(j,static_cast<{self.base.name} &>(obj));')
    for attr in self.attributes:
        if attr.skip_dto: continue
        if attr.optional:
            code.append(f'{indent*1}if(auto it=j.find("{attr.name}"); it!=j.end() and !it->is_null())')
            code.append(f'{indent*2}obj.{attr.name} = *it;')
        else:
            code.append(f'{indent}j.at("{attr.name}").get_to(obj.{attr.name});')
    code.append(f'}}')
    return code

def Struct_to_JSON_string_cpp (self:Struct):
    code = []
    code.append(f'std::string to_json(const {self.name} &obj) {{')
    code.append(f'{indent}json j;')
    code.append(f'{indent}to_json(j,obj);')
    code.append(f'{indent}return j.dump();')
    code.append(f'}}')
    return code

def Struct_from_JSON_string_cpp (self:Struct):
    code = []
    code.append(f'{self.name} {self.name}_from_json(const json &j) {{')
    code.append(f'{indent}{self.name} obj;')
    code.append(f'{indent}from_json(j,obj);')
    code.append(f'{indent}return obj;')
    code.append(f'}}')
    return code

def File_prefix_cpp (objs):
    return [
        f'// {autogen_text}',
        '',
        '#include <optional>',
        '#include <string>',
        '#include <vector>',
        '#include <stdexcept>',
        '#include <cmath> // NAN',
        '',
        '#include <nlohmann/json.hpp>',
        'using json = nlohmann::json;',
        '',
    ]

def Tests_cpp (objs):

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
{obj.name} random_{obj.name} (void) {{
    return {obj.name} (
{random_args}
    );
}}
'''.split('\n'))

        code_construct_random.extend(f'''
std::vector<{obj.name}> random_list_{obj.name} (int min = 0, int max = 3) {{
    const auto size = random_int(min,max);
    std::vector<{obj.name}> list;
    for(int i=0; i<size; i++)
        list.push_back(random_{obj.name}());
    return list;
}}
'''.split('\n'))

        code_construct_random.extend(f'''
std::vector<{obj.name}> random_optional_list_{obj.name} (int min = 0, int max = 3) {{
    if(yes_no())
        return {{}};
    const auto size = random_int(min,max);
    std::vector<{obj.name}> list;
    for(int i=0; i<size; i++)
        list.push_back(random_{obj.name}());
    return list;
}}
'''.split('\n'))

        code_create.append(f'''
        }} else if (struct_name == "{obj.name}") {{
            auto obj1 = random_{obj.name}();
            std::ofstream(file1_path) << to_json(obj1);
            auto obj2 =
                {obj.name}_from_json (
                    json::parse (
                        std::ifstream (
                            file1_path
            )));
            if(obj1!=obj2)
                throw std::runtime_error("Operation 'compare' failed for struct " + struct_name);
''')

        code_convert.extend(f'''
        }} else if (struct_name == "{obj.name}") {{
            auto obj =
                {obj.name}_from_json (
                    json::parse (
                        std::ifstream (
                            file1_path
            )));
            std::ofstream out (file2_path);
            out << to_json(obj);
            if(!out)
                throw std::runtime_error("Operation 'convert': IO error on " + struct_name);
'''.split('\n'))
        code_compare.extend(f'''
        }} else if (struct_name == "{obj.name}") {{
            auto obj1 =
                {obj.name}_from_json (
                    json::parse (
                        std::ifstream (
                            file1_path
            )));
            auto obj2 =
                {obj.name}_from_json (
                    json::parse (
                        std::ifstream (
                            file2_path
            )));
            if(obj1!=obj2)
                throw std::runtime_error("Operation 'compare' failed for struct " + struct_name);
'''.split('\n'))

    code = []
    for line in cpp_test_template.split('\n'):
        if line=='//create-struct-random//':
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

cpp_test_template = '''
#include <random>
#include <limits>
#include <filesystem>
#include <iostream>
#include <fstream>
#include <stdexcept>

#include "dto.cpp"

namespace fs = std::filesystem;

std::random_device rd;
std::mt19937 generator(rd());

int random_int (
    int min = -1000,
    int max = 1000
) {
    std::uniform_int_distribution<int> uniform_dist(min,max);
    return uniform_dist (generator);
}

auto yes_no = [] (void) -> bool {return random_int(0,1);};

std::optional<int> random_optional_int (
    int min = -1000,
    int max = 1000
) {
    if(yes_no())
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
    if(yes_no())
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
    if(can_be_nan and yes_no())
        return NAN;

    if(can_be_infinity and yes_no())
        return (yes_no() ? -1 : 1) * std::numeric_limits<float>::infinity();

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
    if(yes_no())
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
    if(yes_no())
        return random_list_float(len_min,len_max,min,max,can_be_nan,can_be_infinity);
    else
        return {};
}

// https://stackoverflow.com/questions/47977829/generate-a-random-string-in-c11
std::string random_string (int len=16) {
    static std::string str("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz");
    std::shuffle(str.begin(), str.end(), generator);
    return str.substr(0, len);
}

std::optional<std::string> random_optional_string (int len=16) {
    if(yes_no())
        return random_string(len);
    else
        return {};
}

std::vector<std::string> random_list_string (
    int len_min = 0,
    int len_max = 3,
    int strlen_max = 16
) {
    const auto size = random_int (len_min, len_max);
    std::vector<std::string> list;
    for(int i=0; i<size; i++)
        list.push_back(random_string(strlen_max));
    return list;
}

std::optional<std::vector<std::string>> random_optional_list_string (
    int len_min = 0,
    int len_max = 3,
    int strlen_max = 16
) {
    if(yes_no())
        return random_list_string(len_min,len_max,strlen_max);
    else
        return {};
}

//create-struct-random//

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