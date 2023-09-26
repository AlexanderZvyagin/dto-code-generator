#pragma once
// 
// https://github.com/AlexanderZvyagin/dto-code-generator
// Generated by CODE GENERATOR OF DATA TRANSFER OBJECTS (cgdto) version 0.6.4
// 
// Generated from schema: MonteCarlo SDK version (0.2.1)
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
class CashFlows;
std::string CashFlows_to_json_string(const CashFlows &obj);
class CashFlows: public Updater {
public:


    
    CashFlows (
        int underlying = -88,
        std::vector<float> t = {},
        std::string title = ""
    )
    : Updater (
        "CashFlows",
        {underlying},
        t,
        0,
        title
    )
    {
    }

    bool operator == (const CashFlows &other) const {
        if (Updater::operator != (other)) return false;
        return true;
    }
    bool operator != (const CashFlows &other) const {return not(*this==other);}
    std::string json (void) const {
        return CashFlows_to_json_string(*this);
    }
}; // CashFlows
inline
void to_json(json &j, const CashFlows &obj) try {
    j = json::object();
    to_json(j,static_cast<const Updater &>(obj));
} catch (const std::exception &e) {
    std::throw_with_nested(std::runtime_error("void to_json(json &j, const CashFlows &obj) exception"));
}

inline
std::string CashFlows_to_json_string(const CashFlows &obj) {
    json j;
    to_json(j,obj);
    return j.dump();
}
inline
void from_json(const json &j, CashFlows &obj) try {
    from_json(j,static_cast<Updater &>(obj));
} catch (const std::exception &e) {
    std::throw_with_nested(std::runtime_error("void from_json(const json &j, CashFlows &obj) exception"));
}
inline
CashFlows CashFlows_from_json(const json &j) {
    CashFlows obj;
    from_json(j,obj);
    return obj;
}
} // namespace dto

