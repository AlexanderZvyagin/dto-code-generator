#pragma once
// 
// https://github.com/AlexanderZvyagin/dto-code-generator
// Generated by CODE GENERATOR OF DATA TRANSFER OBJECTS (cgdto) version 0.6.2
// 
// Generated from schema: MonteCarlo SDK version (0.2.0)
// 


#include <optional>
#include <string>
#include <vector>
#include <map>
#include <stdexcept>
#include <cmath>

#include <nlohmann/json.hpp>
using json = nlohmann::json;


namespace dto {
class Parameter;
std::string Parameter_to_json_string(const Parameter &obj);
class Parameter {
public:

    float value;
    float step;
    float min;
    float max;

    
    Parameter (
        float value = NAN,
        float step = NAN,
        float min = NAN,
        float max = NAN
    )
    : value (
        value
    )
    , step (
        step
    )
    , min (
        min
    )
    , max (
        max
    )
    {
    }

    bool operator == (const Parameter &other) const {
        if (value != other.value) return false;
        if (step != other.step) return false;
        if (min != other.min) return false;
        if (max != other.max) return false;
        return true;
    }
    bool operator != (const Parameter &other) const {return not(*this==other);}
    std::string json (void) const {
        return Parameter_to_json_string(*this);
    }
}; // Parameter
inline
void to_json(json &j, const Parameter &obj) try {
    j = json::object();
    j["value"] = obj.value;
    j["step"] = obj.step;
    j["min"] = obj.min;
    j["max"] = obj.max;
} catch (const std::exception &e) {
    std::throw_with_nested(std::runtime_error("void to_json(json &j, const Parameter &obj) exception"));
}

inline
std::string Parameter_to_json_string(const Parameter &obj) {
    json j;
    to_json(j,obj);
    return j.dump();
}
inline
void from_json(const json &j, Parameter &obj) try {
    j.at("value").get_to(obj.value);
    j.at("step").get_to(obj.step);
    j.at("min").get_to(obj.min);
    j.at("max").get_to(obj.max);
} catch (const std::exception &e) {
    std::throw_with_nested(std::runtime_error("void from_json(const json &j, Parameter &obj) exception"));
}
inline
Parameter Parameter_from_json(const json &j) {
    Parameter obj;
    from_json(j,obj);
    return obj;
}
} // namespace dto

