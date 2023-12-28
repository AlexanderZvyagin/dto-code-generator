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
class Barrier;
std::string Barrier_to_json_string(const Barrier &obj);
class Barrier: public Updater {
public:

    int DirectionUp {1};
    int DirectionDown {-1};
    int DirectionAny {0};
    int ActionSet {0};

    
    Barrier (
        int underlying = -88,
        float start = NAN,
        float level = NAN,
        int direction = -88,
        int action = -88,
        float value = NAN,
        std::string title = ""
    )
    : Updater (
        "Barrier",
        {underlying},
        {level,value,direction,action},
        {start},
        1,
        title
    )
    {
    }

    bool operator == (const Barrier &other) const {
        if (Updater::operator != (other)) return false;
        return true;
    }
    bool operator != (const Barrier &other) const {return not(*this==other);}
    std::string json (void) const {
        return Barrier_to_json_string(*this);
    }
}; // Barrier
inline
void to_json(json &j, const Barrier &obj) try {
    j = json::object();
    to_json(j,static_cast<const Updater &>(obj));
} catch (const std::exception &e) {
    std::throw_with_nested(std::runtime_error("void to_json(json &j, const Barrier &obj) exception"));
}

inline
std::string Barrier_to_json_string(const Barrier &obj) {
    json j;
    to_json(j,obj);
    return j.dump();
}
inline
void from_json(const json &j, Barrier &obj) try {
    from_json(j,static_cast<Updater &>(obj));
} catch (const std::exception &e) {
    std::throw_with_nested(std::runtime_error("void from_json(const json &j, Barrier &obj) exception"));
}
inline
Barrier Barrier_from_json(const json &j) {
    Barrier obj;
    from_json(j,obj);
    return obj;
}
} // namespace dto

