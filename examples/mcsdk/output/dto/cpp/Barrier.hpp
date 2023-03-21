#pragma once
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


#include "Updater.hpp"
namespace dto {
class Barrier;
std::string Barrier_to_json_string(const Barrier &obj);
class Barrier: public Updater {
public:

    const int DirectionUp = 1;
    const int DirectionDown = -1;
    const int DirectionAny = 0;
    const int ActionSet = 0;

    
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
        start,
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
};
inline
void to_json(json &j, const Barrier &obj) {
    j = json::object();
    to_json(j,static_cast<const Updater &>(obj));
}

inline
std::string Barrier_to_json_string(const Barrier &obj) {
    json j;
    to_json(j,obj);
    return j.dump();
}
inline
void from_json(const json &j, Barrier &obj) {
    from_json(j,static_cast<Updater &>(obj));
}
inline
Barrier Barrier_from_json(const json &j) {
    Barrier obj;
    from_json(j,obj);
    return obj;
}
} // namespace dto

