#pragma once
// 
// https://github.com/AlexanderZvyagin/dto-code-generator
// Generated by CODE GENERATOR OF DATA TRANSFER OBJECTS (cgdto) version 0.6.3
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


#include "UpdaterDto.hpp"
namespace dto {
class Updater;
std::string Updater_to_json_string(const Updater &obj);
class Updater: public UpdaterDto {
public:

    int _equation;
    int _state;
    std::string title;

    
    Updater (
        std::string name = "",
        std::vector<int> refs = {},
        std::vector<float> args = {},
        std::optional<float> start = {},
        std::string title = ""
    )
    : UpdaterDto (
        name,
        refs,
        args,
        start
    )
    , _equation (
        -88
    )
    , _state (
        -88
    )
    , title (
        title
    )
    {
    }

    int GetStateNumber (
    )
    {
        
        if(_state<0)
            throw std::runtime_error("An updater has no state.");
        return _state;
        
    }

    int GetEquationNumber (
    )
    {
        
        if(_equation<0)
            throw std::runtime_error("An updater has no _equation.");
        return _equation;
        
    }

    bool HasState (
    ) const
    {
        
        return start.has_value();
        
    }

    float GetStart (
    ) const
    {
        
        if( not start.has_value() )
            throw std::invalid_argument("start");
        return start.value();
        
    }

    bool operator == (const Updater &other) const {
        if (UpdaterDto::operator != (other)) return false;
        return true;
    }
    bool operator != (const Updater &other) const {return not(*this==other);}
    std::string json (void) const {
        return Updater_to_json_string(*this);
    }
}; // Updater
inline
void to_json(json &j, const Updater &obj) try {
    j = json::object();
    to_json(j,static_cast<const UpdaterDto &>(obj));
} catch (const std::exception &e) {
    std::throw_with_nested(std::runtime_error("void to_json(json &j, const Updater &obj) exception"));
}

inline
std::string Updater_to_json_string(const Updater &obj) {
    json j;
    to_json(j,obj);
    return j.dump();
}
inline
void from_json(const json &j, Updater &obj) try {
    from_json(j,static_cast<UpdaterDto &>(obj));
} catch (const std::exception &e) {
    std::throw_with_nested(std::runtime_error("void from_json(const json &j, Updater &obj) exception"));
}
inline
Updater Updater_from_json(const json &j) {
    Updater obj;
    from_json(j,obj);
    return obj;
}
} // namespace dto

