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
class ZeroCouponBond;
std::string ZeroCouponBond_to_json_string(const ZeroCouponBond &obj);
class ZeroCouponBond: public Updater {
public:


    
    ZeroCouponBond (
        int underlying = -88,
        float start = NAN,
        std::string title = ""
    )
    : Updater (
        "ZeroCouponBond",
        {underlying},
        {},
        start,
        title
    )
    {
    }

    bool operator == (const ZeroCouponBond &other) const {
        if (Updater::operator != (other)) return false;
        return true;
    }
    bool operator != (const ZeroCouponBond &other) const {return not(*this==other);}
    std::string json (void) const {
        return ZeroCouponBond_to_json_string(*this);
    }
}; // ZeroCouponBond
inline
void to_json(json &j, const ZeroCouponBond &obj) try {
    j = json::object();
    to_json(j,static_cast<const Updater &>(obj));
} catch (const std::exception &e) {
    std::throw_with_nested(std::runtime_error("void to_json(json &j, const ZeroCouponBond &obj) exception"));
}

inline
std::string ZeroCouponBond_to_json_string(const ZeroCouponBond &obj) {
    json j;
    to_json(j,obj);
    return j.dump();
}
inline
void from_json(const json &j, ZeroCouponBond &obj) try {
    from_json(j,static_cast<Updater &>(obj));
} catch (const std::exception &e) {
    std::throw_with_nested(std::runtime_error("void from_json(const json &j, ZeroCouponBond &obj) exception"));
}
inline
ZeroCouponBond ZeroCouponBond_from_json(const json &j) {
    ZeroCouponBond obj;
    from_json(j,obj);
    return obj;
}
} // namespace dto

