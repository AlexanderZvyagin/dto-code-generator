#pragma once
// 
// https://github.com/AlexanderZvyagin/dto-code-generator
// Generated by CODE GENERATOR OF DATA TRANSFER OBJECTS (cgdto) version 0.5.1
// 
// Generated from schema: MonteCarlo SDK version (0.1.4)
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
class HistogramAxis;
std::string HistogramAxis_to_json_string(const HistogramAxis &obj);
class HistogramAxis {
public:

    int state;
    int nbins;
    float min;
    float max;

    
    HistogramAxis (
        int _state = -88,
        int _nbins = -88,
        float _min = -88,
        float _max = -88
    )
    : state (
        _state
    )
    , nbins (
        _nbins
    )
    , min (
        _min
    )
    , max (
        _max
    )
    {
    }

    bool operator == (const HistogramAxis &other) const {
        if (state != other.state) return false;
        if (nbins != other.nbins) return false;
        if (min != other.min) return false;
        if (max != other.max) return false;
        return true;
    }
    bool operator != (const HistogramAxis &other) const {return not(*this==other);}
    std::string json (void) const {
        return HistogramAxis_to_json_string(*this);
    }
};
inline
void to_json(json &j, const HistogramAxis &obj) try {
    j = json::object();
    j["state"] = obj.state;
    j["nbins"] = obj.nbins;
    j["min"] = obj.min;
    j["max"] = obj.max;
} catch (const std::exception &e) {
    std::throw_with_nested(std::runtime_error("void to_json(json &j, const HistogramAxis &obj) exception"));
}

inline
std::string HistogramAxis_to_json_string(const HistogramAxis &obj) {
    json j;
    to_json(j,obj);
    return j.dump();
}
inline
void from_json(const json &j, HistogramAxis &obj) try {
    j.at("state").get_to(obj.state);
    j.at("nbins").get_to(obj.nbins);
    j.at("min").get_to(obj.min);
    j.at("max").get_to(obj.max);
} catch (const std::exception &e) {
    std::throw_with_nested(std::runtime_error("void from_json(const json &j, HistogramAxis &obj) exception"));
}
inline
HistogramAxis HistogramAxis_from_json(const json &j) {
    HistogramAxis obj;
    from_json(j,obj);
    return obj;
}
} // namespace dto

