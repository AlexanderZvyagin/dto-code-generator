
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

std::vector<int> random_list_of_ints (
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

std::optional<std::vector<int>> random_optional_list_of_ints (
    int len_min = 0,
    int len_max = 3,
    int int_min = -1000,
    int int_max = 1000
) {
    if(yes_no())
        return random_list_of_ints(len_min,len_max,int_min,int_max);
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

std::vector<float> random_list_of_floats (
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

std::optional<std::vector<float>> random_optional_list_of_floats (
    int   len_min         = 0,
    int   len_max         = 3,
    float min             = -1e6,
    float max             =  1e6,
    bool  can_be_nan      = false,
    bool  can_be_infinity = false
) {
    if(yes_no())
        return random_list_of_floats(len_min,len_max,min,max,can_be_nan,can_be_infinity);
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

std::vector<std::string> random_list_of_strings (
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

std::optional<std::vector<std::string>> random_optional_list_of_strings (
    int len_min = 0,
    int len_max = 3,
    int strlen_max = 16
) {
    if(yes_no())
        return random_list_of_strings(len_min,len_max,strlen_max);
    else
        {};
}


UpdaterDoc random_UpdaterDoc (void) {
    return UpdaterDoc (
        random_string(),
        random_string(),
        random_string(),
        random_string(),
        random_int(),
        random_int()

    );
}


std::vector<UpdaterDoc> random_list_of_UpdaterDoc (int min = 0, int max = 3) {
    const auto size = random_int(min,max);
    std::vector<UpdaterDoc> list;
    for(int i=0; i<size; i++)
        list.push_back(random_UpdaterDoc());
    return list;
}


std::vector<UpdaterDoc> random_optional_list_of_UpdaterDoc (int min = 0, int max = 3) {
    if(yes_no())
        return {};
    const auto size = random_int(min,max);
    std::vector<UpdaterDoc> list;
    for(int i=0; i<size; i++)
        list.push_back(random_UpdaterDoc());
    return list;
}


UpdaterDto random_UpdaterDto (void) {
    return UpdaterDto (
        random_string(),
        random_list_of_ints(),
        random_list_of_floats(),
        random_optional_float()

    );
}


std::vector<UpdaterDto> random_list_of_UpdaterDto (int min = 0, int max = 3) {
    const auto size = random_int(min,max);
    std::vector<UpdaterDto> list;
    for(int i=0; i<size; i++)
        list.push_back(random_UpdaterDto());
    return list;
}


std::vector<UpdaterDto> random_optional_list_of_UpdaterDto (int min = 0, int max = 3) {
    if(yes_no())
        return {};
    const auto size = random_int(min,max);
    std::vector<UpdaterDto> list;
    for(int i=0; i<size; i++)
        list.push_back(random_UpdaterDto());
    return list;
}


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

        } else if (struct_name == "UpdaterDoc") {
            f << to_json(random_UpdaterDoc());


        } else if (struct_name == "UpdaterDto") {
            f << to_json(random_UpdaterDto());

        } else {
            throw std::runtime_error("Not supported operation 'create' on struct " + struct_name);
        }
        if(!f)
            throw std::runtime_error("Operation 'create': IO error");

    } else if (command == "convert") {

        if (false) {

        } else if (struct_name == "UpdaterDoc") {
            auto obj =
                UpdaterDoc_from_json (
                    json::parse (
                        std::ifstream (
                            file1_path
            )));
            std::ofstream out (file2_path);
            out << to_json(obj);
            if(!out)
                throw std::runtime_error("Operation 'convert': IO error on " + struct_name);


        } else if (struct_name == "UpdaterDto") {
            auto obj =
                UpdaterDto_from_json (
                    json::parse (
                        std::ifstream (
                            file1_path
            )));
            std::ofstream out (file2_path);
            out << to_json(obj);
            if(!out)
                throw std::runtime_error("Operation 'convert': IO error on " + struct_name);

        } else {
            throw std::runtime_error("Not supported operation 'convert' on struct " + struct_name);
        }

    } else if (command == "compare") {

        if (false) {

        } else if (struct_name == "UpdaterDoc") {
            auto obj1 =
                UpdaterDoc_from_json (
                    json::parse (
                        std::ifstream (
                            file1_path
            )));
            auto obj2 =
                UpdaterDoc_from_json (
                    json::parse (
                        std::ifstream (
                            file2_path
            )));
            if(obj1!=obj2)
                throw std::runtime_error("Operation 'compare' failed for struct " + struct_name);


        } else if (struct_name == "UpdaterDto") {
            auto obj1 =
                UpdaterDto_from_json (
                    json::parse (
                        std::ifstream (
                            file1_path
            )));
            auto obj2 =
                UpdaterDto_from_json (
                    json::parse (
                        std::ifstream (
                            file2_path
            )));
            if(obj1!=obj2)
                throw std::runtime_error("Operation 'compare' failed for struct " + struct_name);

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

