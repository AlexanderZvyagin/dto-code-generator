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


#include "Updater.hpp"
namespace dto {
class Linear1DInterpolation;
std::string Linear1DInterpolation_to_json_string(const Linear1DInterpolation &obj);
class Linear1DInterpolation: public Updater {
public:


    
    Linear1DInterpolation (
        int ref = -88,
        float xmin = -1,
        float xmax = 1,
        std::vector<float> y = {},
        std::string title = ""
    )
    : Updater (
        "Linear1DInterpolation",
        {ref},
        {},
        0,
        title
    )
    {
        
        if(y.size()<2)
            throw std::invalid_argument("Linear1DInterpolation: y-vector must have at least 2 elements: y(xmin), y(xmax)");
        args.value() = std::vector<float>();
        args.value().reserve(2+y.size());
        args.value().push_back(xmin);
        args.value().push_back(xmax);
        for(auto item: y)
            args.value().push_back(item);
        
    }

    bool operator == (const Linear1DInterpolation &other) const {
        if (Updater::operator != (other)) return false;
        return true;
    }
    bool operator != (const Linear1DInterpolation &other) const {return not(*this==other);}
    std::string json (void) const {
        return Linear1DInterpolation_to_json_string(*this);
    }
};
inline
void to_json(json &j, const Linear1DInterpolation &obj) try {
    j = json::object();
    to_json(j,static_cast<const Updater &>(obj));
} catch (const std::exception &e) {
    std::throw_with_nested(std::runtime_error("void to_json(json &j, const Linear1DInterpolation &obj) exception"));
}

inline
std::string Linear1DInterpolation_to_json_string(const Linear1DInterpolation &obj) {
    json j;
    to_json(j,obj);
    return j.dump();
}
inline
void from_json(const json &j, Linear1DInterpolation &obj) try {
    from_json(j,static_cast<Updater &>(obj));
} catch (const std::exception &e) {
    std::throw_with_nested(std::runtime_error("void from_json(const json &j, Linear1DInterpolation &obj) exception"));
}
inline
Linear1DInterpolation Linear1DInterpolation_from_json(const json &j) {
    Linear1DInterpolation obj;
    from_json(j,obj);
    return obj;
}
} // namespace dto

