#pragma once
// 
// https://gitlab.com/zvyagin.alexander/dto-code-generator
// Generated by CODE GENERATOR OF DATA TRANSFER OBJECTS (cgdto) version 0.4.2
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
class Option;
std::string Option_to_json_string(const Option &obj);
class Option: public Updater {
public:

    const int Call = 0;
    const int Put = 1;

    
    Option (
        int underlying = -88,
        float strike = NAN,
        int call_put = -88,
        std::string title = ""
    )
    : Updater (
        "Option",
        {underlying},
        {strike,call_put},
        0,
        title
    )
    {
    }

    bool operator == (const Option &other) const {
        if (Updater::operator != (other)) return false;
        return true;
    }
    bool operator != (const Option &other) const {return not(*this==other);}
    std::string json (void) const {
        return Option_to_json_string(*this);
    }
};
inline
void to_json(json &j, const Option &obj) try {
    j = json::object();
    to_json(j,static_cast<const Updater &>(obj));
} catch (const std::exception &e) {
    std::throw_with_nested(std::runtime_error("void to_json(json &j, const Option &obj) exception"));
}

inline
std::string Option_to_json_string(const Option &obj) {
    json j;
    to_json(j,obj);
    return j.dump();
}
inline
void from_json(const json &j, Option &obj) try {
    from_json(j,static_cast<Updater &>(obj));
} catch (const std::exception &e) {
    std::throw_with_nested(std::runtime_error("void from_json(const json &j, Option &obj) exception"));
}
inline
Option Option_from_json(const json &j) {
    Option obj;
    from_json(j,obj);
    return obj;
}
} // namespace dto

