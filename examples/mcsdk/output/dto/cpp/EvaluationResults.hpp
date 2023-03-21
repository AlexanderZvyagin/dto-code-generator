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

#include <nlohmann/json.hpp>
using json = nlohmann::json;


#include "Model.hpp"
#include "Histogram.hpp"
namespace dto {
class EvaluationResults;
std::string EvaluationResults_to_json_string(const EvaluationResults &obj);
class EvaluationResults {
public:

    std::vector<std::string> names;
    std::vector<int> npaths;
    std::vector<float> mean;
    std::vector<float> stddev;
    std::vector<float> skewness;
    std::vector<float> time_points;
    std::vector<int> time_steps;
    std::vector<Histogram> histograms;
    std::optional<Model> model;

    
    EvaluationResults (
        std::vector<std::string> names = {},
        std::vector<int> npaths = {},
        std::vector<float> mean = {},
        std::vector<float> stddev = {},
        std::vector<float> skewness = {},
        std::vector<float> time_points = {},
        std::vector<int> time_steps = {},
        std::vector<Histogram> histograms = {},
        std::optional<Model> model = {}
    )
    : names (
        names
    )
    , npaths (
        npaths
    )
    , mean (
        mean
    )
    , stddev (
        stddev
    )
    , skewness (
        skewness
    )
    , time_points (
        time_points
    )
    , time_steps (
        time_steps
    )
    , histograms (
        histograms
    )
    , model (
        model
    )
    {
    }

    int GetNumberOfStates (
    ) const
    {
        
        return names.size();
        
    }

    int GetNumberOfEvaluations (
    ) const
    {
        
        return time_points.size();
        
    }

    int Index (
        int state,
        int point
    ) const
    {
        
        if( not (state>=0 and state<GetNumberOfStates() and point>=0 and point<GetNumberOfEvaluations()) )
            throw std::invalid_argument("Index");
        return point*GetNumberOfStates() + state;
        
    }

    Result GetStateEvaluationResult (
        int state,
        int point
    ) const
    {
        
        auto n = Index(state,point);
        return Result(npaths[n],mean[n],stddev[n],skewness[n]);
        
    }

    bool operator == (const EvaluationResults &other) const {
        if (names != other.names) return false;
        if (npaths != other.npaths) return false;
        if (mean != other.mean) return false;
        if (stddev != other.stddev) return false;
        if (skewness != other.skewness) return false;
        if (time_points != other.time_points) return false;
        if (time_steps != other.time_steps) return false;
        if (histograms != other.histograms) return false;
        if (model != other.model) return false;
        return true;
    }
    bool operator != (const EvaluationResults &other) const {return not(*this==other);}
    std::string json (void) const {
        return EvaluationResults_to_json_string(*this);
    }
};
inline
void to_json(json &j, const EvaluationResults &obj) {
    j = json::object();
    j["names"] = obj.names;
    j["npaths"] = obj.npaths;
    j["mean"] = obj.mean;
    j["stddev"] = obj.stddev;
    j["skewness"] = obj.skewness;
    j["time_points"] = obj.time_points;
    j["time_steps"] = obj.time_steps;
    j["histograms"] = obj.histograms;
    if(obj.model.has_value())
        j["model"] = obj.model.value();
}

inline
std::string EvaluationResults_to_json_string(const EvaluationResults &obj) {
    json j;
    to_json(j,obj);
    return j.dump();
}
inline
void from_json(const json &j, EvaluationResults &obj) {
    j.at("names").get_to(obj.names);
    j.at("npaths").get_to(obj.npaths);
    j.at("mean").get_to(obj.mean);
    j.at("stddev").get_to(obj.stddev);
    j.at("skewness").get_to(obj.skewness);
    j.at("time_points").get_to(obj.time_points);
    j.at("time_steps").get_to(obj.time_steps);
    j.at("histograms").get_to(obj.histograms);
    if(auto it=j.find("model"); it!=j.end() and !it->is_null())
        obj.model = *it;
}
inline
EvaluationResults EvaluationResults_from_json(const json &j) {
    EvaluationResults obj;
    from_json(j,obj);
    return obj;
}
} // namespace dto

