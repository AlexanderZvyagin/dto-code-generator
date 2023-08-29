#pragma once
// 
// https://github.com/AlexanderZvyagin/dto-code-generator
// Generated by CODE GENERATOR OF DATA TRANSFER OBJECTS (cgdto) version 0.6.0
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


#include "Updater.hpp"
namespace dto {
class SumOnIntervals;
std::string SumOnIntervals_to_json_string(const SumOnIntervals &obj);
class SumOnIntervals: public Updater {
public:


    
    SumOnIntervals (
        int notional = -88,
        std::vector<float> t = {},
        std::string title = ""
    )
    : Updater (
        "SumOnIntervals",
        {notional},
        t,
        0,
        title
    )
    {
    }

    bool operator == (const SumOnIntervals &other) const {
        if (Updater::operator != (other)) return false;
        return true;
    }
    bool operator != (const SumOnIntervals &other) const {return not(*this==other);}
    std::string json (void) const {
        return SumOnIntervals_to_json_string(*this);
    }
}; // SumOnIntervals
inline
void to_json(json &j, const SumOnIntervals &obj) try {
    j = json::object();
    to_json(j,static_cast<const Updater &>(obj));
} catch (const std::exception &e) {
    std::throw_with_nested(std::runtime_error("void to_json(json &j, const SumOnIntervals &obj) exception"));
}

inline
std::string SumOnIntervals_to_json_string(const SumOnIntervals &obj) {
    json j;
    to_json(j,obj);
    return j.dump();
}
inline
void from_json(const json &j, SumOnIntervals &obj) try {
    from_json(j,static_cast<Updater &>(obj));
} catch (const std::exception &e) {
    std::throw_with_nested(std::runtime_error("void from_json(const json &j, SumOnIntervals &obj) exception"));
}
inline
SumOnIntervals SumOnIntervals_from_json(const json &j) {
    SumOnIntervals obj;
    from_json(j,obj);
    return obj;
}
} // namespace dto

