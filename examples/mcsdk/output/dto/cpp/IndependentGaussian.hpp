#pragma once
// 
// https://github.com/AlexanderZvyagin/dto-code-generator
// Generated by CODE GENERATOR OF DATA TRANSFER OBJECTS (cgdto) version 0.7.1
// 
// Generated from schema: MonteCarlo SDK version (0.5.0)
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
class IndependentGaussian;
std::string IndependentGaussian_to_json_string(const IndependentGaussian &obj);
class IndependentGaussian: public Updater {
public:


    
    IndependentGaussian (
        std::vector<int> refs = {},
        std::string title = ""
    )
    : Updater (
        "IndependentGaussian",
        refs,
        {},
        {},
        title
    )
    {
    }

    bool operator == (const IndependentGaussian &other) const {
        if (Updater::operator != (other)) return false;
        return true;
    }
    bool operator != (const IndependentGaussian &other) const {return not(*this==other);}
    std::string json (void) const {
        return IndependentGaussian_to_json_string(*this);
    }
}; // IndependentGaussian
inline
void to_json(json &j, const IndependentGaussian &obj) try {
    j = json::object();
    to_json(j,static_cast<const Updater &>(obj));
} catch (const std::exception &e) {
    std::throw_with_nested(std::runtime_error("void to_json(json &j, const IndependentGaussian &obj) exception"));
}

inline
std::string IndependentGaussian_to_json_string(const IndependentGaussian &obj) {
    json j;
    to_json(j,obj);
    return j.dump();
}
inline
void from_json(const json &j, IndependentGaussian &obj) try {
    from_json(j,static_cast<Updater &>(obj));
} catch (const std::exception &e) {
    std::throw_with_nested(std::runtime_error("void from_json(const json &j, IndependentGaussian &obj) exception"));
}
inline
IndependentGaussian IndependentGaussian_from_json(const json &j) {
    IndependentGaussian obj;
    from_json(j,obj);
    return obj;
}
} // namespace dto

