#pragma once
// 
// https://github.com/AlexanderZvyagin/dto-code-generator
// Generated by CODE GENERATOR OF DATA TRANSFER OBJECTS (cgdto) version 0.8.0
// 
// Generated from schema: MonteCarlo SDK version (0.6.4-dev-versioning)
// 


#include <optional>
#include <string>
#include <vector>
#include <map>
#include <stdexcept>
#include <cmath>

#include <nlohmann/json.hpp>
using json = nlohmann::json;


#include "Updater.hpp"
namespace dto {
class Sum;
std::string Sum_to_json_string(const Sum &obj);
class Sum: public Updater {
public:


    
    Sum (
        std::vector<float> weights = {},
        std::vector<int> states = {},
        std::string title = ""
    )
    : Updater (
        "Sum",
        states,
        weights,
        {},
        1,
        title
    )
    {
    }

    bool operator == (const Sum &other) const {
        if (Updater::operator != (other)) return false;
        return true;
    }
    bool operator != (const Sum &other) const {return not(*this==other);}
    std::string json (void) const {
        return Sum_to_json_string(*this);
    }
}; // Sum
inline
void to_json(json &j, const Sum &obj) try {
    j = json::object();
    to_json(j,static_cast<const Updater &>(obj));
} catch (const std::exception &e) {
    std::throw_with_nested(std::runtime_error("void to_json(json &j, const Sum &obj) exception"));
}

inline
std::string Sum_to_json_string(const Sum &obj) {
    json j;
    to_json(j,obj);
    return j.dump();
}
inline
void from_json(const json &j, Sum &obj) try {
    from_json(j,static_cast<Updater &>(obj));
} catch (const std::exception &e) {
    std::throw_with_nested(std::runtime_error("void from_json(const json &j, Sum &obj) exception"));
}
inline
Sum Sum_from_json(const json &j) {
    Sum obj;
    from_json(j,obj);
    return obj;
}
} // namespace dto

