// 
// https://gitlab.com/zvyagin.alexander/dto-code-generator
// Generated by CODE GENERATOR OF DATA TRANSFER OBJECTS (cgdto) version 0.4.0
// 
//         Generated from: MonteCarlo SDK version (0.2.0)
//         


#include <optional>
#include <string>
#include <vector>
#include <map>
#include <stdexcept>
#include <cmath>

#include "json.hpp"
using json = nlohmann::json;


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
void to_json(json &j, const HistogramAxis &obj) {
    j = json::object();
    j["state"] = obj.state;
    j["nbins"] = obj.nbins;
    j["min"] = obj.min;
    j["max"] = obj.max;
}

inline
std::string HistogramAxis_to_json_string(const HistogramAxis &obj) {
    json j;
    to_json(j,obj);
    return j.dump();
}
inline
void from_json(const json &j, HistogramAxis &obj) {
    j.at("state").get_to(obj.state);
    j.at("nbins").get_to(obj.nbins);
    j.at("min").get_to(obj.min);
    j.at("max").get_to(obj.max);
}
inline
HistogramAxis HistogramAxis_from_json(const json &j) {
    HistogramAxis obj;
    from_json(j,obj);
    return obj;
}

