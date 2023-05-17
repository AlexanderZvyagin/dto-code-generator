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


namespace dto {
class Result;
std::string Result_to_json_string(const Result &obj);
class Result {
public:

    int n;
    float mean;
    float stddev;
    float skewness;

    
    Result (
        int n = 0,
        float mean = NAN,
        float stddev = NAN,
        float skewness = NAN
    )
    : n (
        n
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
    {
    }

    float GetMean (
    ) const
    {
        
        return mean;
        
    }

    float GetMeanError (
    ) const
    {
        
        return n<=0 ? NAN : stddev/std::sqrt(n);
        
    }

    float GetStdDev (
    ) const
    {
        
        return stddev;
        
    }

    float GetSkewness (
    ) const
    {
        
        return skewness;
        
    }

    bool operator == (const Result &other) const {
        if (n != other.n) return false;
        if (mean != other.mean) return false;
        if (stddev != other.stddev) return false;
        if (skewness != other.skewness) return false;
        return true;
    }
    bool operator != (const Result &other) const {return not(*this==other);}
    std::string json (void) const {
        return Result_to_json_string(*this);
    }
};
inline
void to_json(json &j, const Result &obj) try {
    j = json::object();
    j["n"] = obj.n;
    j["mean"] = obj.mean;
    j["stddev"] = obj.stddev;
    j["skewness"] = obj.skewness;
} catch (const std::exception &e) {
    std::throw_with_nested(std::runtime_error("void to_json(json &j, const Result &obj) exception"));
}

inline
std::string Result_to_json_string(const Result &obj) {
    json j;
    to_json(j,obj);
    return j.dump();
}
inline
void from_json(const json &j, Result &obj) try {
    j.at("n").get_to(obj.n);
    j.at("mean").get_to(obj.mean);
    j.at("stddev").get_to(obj.stddev);
    j.at("skewness").get_to(obj.skewness);
} catch (const std::exception &e) {
    std::throw_with_nested(std::runtime_error("void from_json(const json &j, Result &obj) exception"));
}
inline
Result Result_from_json(const json &j) {
    Result obj;
    from_json(j,obj);
    return obj;
}
} // namespace dto

