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
#include "EvaluationPoint.hpp"
namespace dto {
class Model;
std::string Model_to_json_string(const Model &obj);
class Model {
public:

    float TimeStart;
    int TimeSteps;
    int NumPaths;
    std::vector<Updater> updaters;
    std::vector<EvaluationPoint> evaluations;
    int RandomSeed;
    float RunTimeoutSeconds;
    int MemoryLimitKB;
    std::map<int,std::string> titles;

    
    Model (
        float TimeStart = NAN,
        int TimeSteps = 0,
        int NumPaths = 0,
        std::vector<Updater> updaters = {},
        std::vector<EvaluationPoint> evaluations = {},
        int RandomSeed = -1,
        float RunTimeoutSeconds = 1,
        int MemoryLimitKB = 1
    )
    : TimeStart (
        TimeStart
    )
    , TimeSteps (
        TimeSteps
    )
    , NumPaths (
        NumPaths
    )
    , updaters (
        updaters
    )
    , evaluations (
        evaluations
    )
    , RandomSeed (
        RandomSeed
    )
    , RunTimeoutSeconds (
        RunTimeoutSeconds
    )
    , MemoryLimitKB (
        MemoryLimitKB
    )
    {
    }

    int GetNumberOfUpdaters (
    ) const
    {
        
        return updaters.size();
        
    }

    int GetNumberOfStates (
    ) const
    {
        
        int n {0};
        for(const auto &u: updaters)
            n += u.HasState();
        return n;
        
    }

    Updater Add (
        Updater updater
    )
    {
        
        updaters.push_back(updater);
        auto &u = updaters.back();
        u._equation = GetNumberOfUpdaters()-1;
        if(u.HasState()){
            u._state = GetNumberOfStates()-1;
            titles[u._state] = u.title;
        }
        return u;
        
    }

    bool operator == (const Model &other) const {
        if (TimeStart != other.TimeStart) return false;
        if (TimeSteps != other.TimeSteps) return false;
        if (NumPaths != other.NumPaths) return false;
        if (updaters != other.updaters) return false;
        if (evaluations != other.evaluations) return false;
        if (RandomSeed != other.RandomSeed) return false;
        if (RunTimeoutSeconds != other.RunTimeoutSeconds) return false;
        if (MemoryLimitKB != other.MemoryLimitKB) return false;
        return true;
    }
    bool operator != (const Model &other) const {return not(*this==other);}
    std::string json (void) const {
        return Model_to_json_string(*this);
    }
}; // Model
inline
void to_json(json &j, const Model &obj) try {
    j = json::object();
    j["TimeStart"] = obj.TimeStart;
    j["TimeSteps"] = obj.TimeSteps;
    j["NumPaths"] = obj.NumPaths;
    j["updaters"] = obj.updaters;
    j["evaluations"] = obj.evaluations;
    j["RandomSeed"] = obj.RandomSeed;
    j["RunTimeoutSeconds"] = obj.RunTimeoutSeconds;
    j["MemoryLimitKB"] = obj.MemoryLimitKB;
} catch (const std::exception &e) {
    std::throw_with_nested(std::runtime_error("void to_json(json &j, const Model &obj) exception"));
}

inline
std::string Model_to_json_string(const Model &obj) {
    json j;
    to_json(j,obj);
    return j.dump();
}
inline
void from_json(const json &j, Model &obj) try {
    j.at("TimeStart").get_to(obj.TimeStart);
    j.at("TimeSteps").get_to(obj.TimeSteps);
    j.at("NumPaths").get_to(obj.NumPaths);
    j.at("updaters").get_to(obj.updaters);
    j.at("evaluations").get_to(obj.evaluations);
    j.at("RandomSeed").get_to(obj.RandomSeed);
    j.at("RunTimeoutSeconds").get_to(obj.RunTimeoutSeconds);
    j.at("MemoryLimitKB").get_to(obj.MemoryLimitKB);
} catch (const std::exception &e) {
    std::throw_with_nested(std::runtime_error("void from_json(const json &j, Model &obj) exception"));
}
inline
Model Model_from_json(const json &j) {
    Model obj;
    from_json(j,obj);
    return obj;
}
} // namespace dto

