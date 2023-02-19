// This is an automatically generated file.

#include <optional>
#include <string>
#include <vector>
#include <stdexcept>
#include <cmath> // NAN

#include <nlohmann/json.hpp>
using json = nlohmann::json;

class UpdaterDoc {
public:

    std::string name;
    std::string title;
    std::string doc_md;
    std::string start;
    int nargs_min;
    int nrefs_min;

    
    UpdaterDoc (
        std::string name_ = "",
        std::string title_ = "",
        std::string doc_md_ = "",
        std::string start_ = "",
        int nargs_min_ = -88,
        int nrefs_min_ = -88
    )
    : name (
        name_
    )
    , title (
        title_
    )
    , doc_md (
        doc_md_
    )
    , start (
        start_
    )
    , nargs_min (
        nargs_min_
    )
    , nrefs_min (
        nrefs_min_
    )
    {
    }

    bool operator == (const UpdaterDoc &other) const {
        if (name != other.name) return false;
        if (title != other.title) return false;
        if (doc_md != other.doc_md) return false;
        if (start != other.start) return false;
        if (nargs_min != other.nargs_min) return false;
        if (nrefs_min != other.nrefs_min) return false;
        return true;
    }
    bool operator != (const UpdaterDoc &other) const {return not(*this==other);}
};
void to_json(json &j, const UpdaterDoc &obj) {
    j["name"] = obj.name;
    j["title"] = obj.title;
    j["doc_md"] = obj.doc_md;
    j["start"] = obj.start;
    j["nargs_min"] = obj.nargs_min;
    j["nrefs_min"] = obj.nrefs_min;
}

std::string to_json(const UpdaterDoc &obj) {
    json j;
    to_json(j,obj);
    return j.dump();
}
void from_json(const json &j, UpdaterDoc &obj) {
    j.at("name").get_to(obj.name);
    j.at("title").get_to(obj.title);
    j.at("doc_md").get_to(obj.doc_md);
    j.at("start").get_to(obj.start);
    j.at("nargs_min").get_to(obj.nargs_min);
    j.at("nrefs_min").get_to(obj.nrefs_min);
}
UpdaterDoc UpdaterDoc_from_json(const json &j) {
    UpdaterDoc obj;
    from_json(j,obj);
    return obj;
}

class UpdaterDto {
public:

    std::string name;
    std::optional<std::vector<int>> refs;
    std::optional<std::vector<float>> args;
    std::optional<float> start;

    
    UpdaterDto (
        std::string name_ = "",
        std::optional<std::vector<int>> refs_ = {},
        std::optional<std::vector<float>> args_ = {},
        std::optional<float> start_ = {}
    )
    : name (
        name_
    )
    , refs (
        refs_
    )
    , args (
        args_
    )
    , start (
        start_
    )
    {
    }

    bool operator == (const UpdaterDto &other) const {
        if (name != other.name) return false;
        if (refs != other.refs) return false;
        if (args != other.args) return false;
        if (start != other.start) return false;
        return true;
    }
    bool operator != (const UpdaterDto &other) const {return not(*this==other);}
};
void to_json(json &j, const UpdaterDto &obj) {
    j["name"] = obj.name;
    if(obj.refs.has_value())
        j["refs"] = obj.refs.value();
    if(obj.args.has_value())
        j["args"] = obj.args.value();
    if(obj.start.has_value())
        j["start"] = obj.start.value();
}

std::string to_json(const UpdaterDto &obj) {
    json j;
    to_json(j,obj);
    return j.dump();
}
void from_json(const json &j, UpdaterDto &obj) {
    j.at("name").get_to(obj.name);
    if(auto it=j.find("refs"); it!=j.end() and !it->is_null())
        obj.refs = *it;
    if(auto it=j.find("args"); it!=j.end() and !it->is_null())
        obj.args = *it;
    if(auto it=j.find("start"); it!=j.end() and !it->is_null())
        obj.start = *it;
}
UpdaterDto UpdaterDto_from_json(const json &j) {
    UpdaterDto obj;
    from_json(j,obj);
    return obj;
}

class Updater: public UpdaterDto {
public:

    int _equation;
    int _state;

    
    Updater (
        std::string name = "",
        std::vector<int> refs = {},
        std::vector<float> args = {},
        float start = NAN
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
    {
    }

    int GetStateNumber (
    )
    {
        
        if(_state<0)
            throw std::runtime_error("An updater has no state.");
        return _state;
        
    }

    bool HasState (
    ) const
    {
        
        return _state>=0;
        
    }

    bool operator == (const Updater &other) const {
        if (UpdaterDto::operator != (other)) return false;
        if (_equation != other._equation) return false;
        if (_state != other._state) return false;
        return true;
    }
    bool operator != (const Updater &other) const {return not(*this==other);}
};
void to_json(json &j, const Updater &obj) {
    to_json(j,static_cast<const UpdaterDto &>(obj));
}

std::string to_json(const Updater &obj) {
    json j;
    to_json(j,obj);
    return j.dump();
}
void from_json(const json &j, Updater &obj) {
    from_json(j,static_cast<UpdaterDto &>(obj));
}
Updater Updater_from_json(const json &j) {
    Updater obj;
    from_json(j,obj);
    return obj;
}


void from_json(const json &j, std::vector<Updater> &u) {
    for(auto v: j)
        u.push_back(v);
}

class IndependentGaussian: public Updater {
public:


    
    IndependentGaussian (
        std::vector<int> refs_ = {}
    )
    : Updater (
        "IndependentGaussian",
        refs_,
        {},
        -88
    )
    {
    }

    bool operator == (const IndependentGaussian &other) const {
        if (Updater::operator != (other)) return false;
        return true;
    }
    bool operator != (const IndependentGaussian &other) const {return not(*this==other);}
};
void to_json(json &j, const IndependentGaussian &obj) {
    to_json(j,static_cast<const Updater &>(obj));
}

std::string to_json(const IndependentGaussian &obj) {
    json j;
    to_json(j,obj);
    return j.dump();
}
void from_json(const json &j, IndependentGaussian &obj) {
    from_json(j,static_cast<Updater &>(obj));
}
IndependentGaussian IndependentGaussian_from_json(const json &j) {
    IndependentGaussian obj;
    from_json(j,obj);
    return obj;
}

class CorrelatedGaussian: public Updater {
public:


    
    CorrelatedGaussian (
        float correlation = NAN,
        int state1 = -88,
        int state2 = -88
    )
    : Updater (
        "CorrelatedGaussian",
        {state1,state2},
        {correlation},
        -88
    )
    {
    }

    bool operator == (const CorrelatedGaussian &other) const {
        if (Updater::operator != (other)) return false;
        return true;
    }
    bool operator != (const CorrelatedGaussian &other) const {return not(*this==other);}
};
void to_json(json &j, const CorrelatedGaussian &obj) {
    to_json(j,static_cast<const Updater &>(obj));
}

std::string to_json(const CorrelatedGaussian &obj) {
    json j;
    to_json(j,obj);
    return j.dump();
}
void from_json(const json &j, CorrelatedGaussian &obj) {
    from_json(j,static_cast<Updater &>(obj));
}
CorrelatedGaussian CorrelatedGaussian_from_json(const json &j) {
    CorrelatedGaussian obj;
    from_json(j,obj);
    return obj;
}

class Barrier: public Updater {
public:


    
    Barrier (
        int underlying = -88,
        float start = NAN,
        float level = NAN,
        int direction = -88,
        int action = -88,
        float value = NAN
    )
    : Updater (
        "Barrier",
        {underlying},
        {level,value,direction,action},
        start
    )
    {
    }

    bool operator == (const Barrier &other) const {
        if (Updater::operator != (other)) return false;
        return true;
    }
    bool operator != (const Barrier &other) const {return not(*this==other);}
};
void to_json(json &j, const Barrier &obj) {
    to_json(j,static_cast<const Updater &>(obj));
}

std::string to_json(const Barrier &obj) {
    json j;
    to_json(j,obj);
    return j.dump();
}
void from_json(const json &j, Barrier &obj) {
    from_json(j,static_cast<Updater &>(obj));
}
Barrier Barrier_from_json(const json &j) {
    Barrier obj;
    from_json(j,obj);
    return obj;
}

class HistogramAxis {
public:

    int state;
    int nbins;
    float min;
    float max;

    
    HistogramAxis (
        int _state = -88,
        int _nbins = -88,
        float _min = -88,
        float _max = -88
    )
    : state (
        _state
    )
    , nbins (
        _nbins
    )
    , min (
        _min
    )
    , max (
        _max
    )
    {
    }

    bool operator == (const HistogramAxis &other) const {
        if (state != other.state) return false;
        if (nbins != other.nbins) return false;
        if (min != other.min) return false;
        if (max != other.max) return false;
        return true;
    }
    bool operator != (const HistogramAxis &other) const {return not(*this==other);}
};
void to_json(json &j, const HistogramAxis &obj) {
    j["state"] = obj.state;
    j["nbins"] = obj.nbins;
    j["min"] = obj.min;
    j["max"] = obj.max;
}

std::string to_json(const HistogramAxis &obj) {
    json j;
    to_json(j,obj);
    return j.dump();
}
void from_json(const json &j, HistogramAxis &obj) {
    j.at("state").get_to(obj.state);
    j.at("nbins").get_to(obj.nbins);
    j.at("min").get_to(obj.min);
    j.at("max").get_to(obj.max);
}
HistogramAxis HistogramAxis_from_json(const json &j) {
    HistogramAxis obj;
    from_json(j,obj);
    return obj;
}

class Histogram {
public:

    HistogramAxis x;
    HistogramAxis y;

    
    Histogram (
        HistogramAxis x = HistogramAxis(),
        HistogramAxis y = HistogramAxis()
    )
    : x (
        x
    )
    , y (
        y
    )
    {
    }

    bool operator == (const Histogram &other) const {
        if (x != other.x) return false;
        if (y != other.y) return false;
        return true;
    }
    bool operator != (const Histogram &other) const {return not(*this==other);}
};
void to_json(json &j, const Histogram &obj) {
    j["x"] = obj.x;
    j["y"] = obj.y;
}

std::string to_json(const Histogram &obj) {
    json j;
    to_json(j,obj);
    return j.dump();
}
void from_json(const json &j, Histogram &obj) {
    j.at("x").get_to(obj.x);
    j.at("y").get_to(obj.y);
}
Histogram Histogram_from_json(const json &j) {
    Histogram obj;
    from_json(j,obj);
    return obj;
}


void from_json(const json &j, std::vector<Histogram> &u) {
    for(auto v: j)
        u.push_back(v);
}

class EvaluationPoint {
public:

    int state;
    float time;
    float value;
    float error;

    
    EvaluationPoint (
        int state_ = -88,
        float time_ = NAN,
        float value_ = NAN,
        float error_ = NAN
    )
    : state (
        state_
    )
    , time (
        time_
    )
    , value (
        value_
    )
    , error (
        error_
    )
    {
    }

    bool operator == (const EvaluationPoint &other) const {
        if (state != other.state) return false;
        if (time != other.time) return false;
        if (value != other.value) return false;
        if (error != other.error) return false;
        return true;
    }
    bool operator != (const EvaluationPoint &other) const {return not(*this==other);}
};
void to_json(json &j, const EvaluationPoint &obj) {
    j["state"] = obj.state;
    j["time"] = obj.time;
    j["value"] = obj.value;
    j["error"] = obj.error;
}

std::string to_json(const EvaluationPoint &obj) {
    json j;
    to_json(j,obj);
    return j.dump();
}
void from_json(const json &j, EvaluationPoint &obj) {
    j.at("state").get_to(obj.state);
    j.at("time").get_to(obj.time);
    j.at("value").get_to(obj.value);
    j.at("error").get_to(obj.error);
}
EvaluationPoint EvaluationPoint_from_json(const json &j) {
    EvaluationPoint obj;
    from_json(j,obj);
    return obj;
}

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

    
    EvaluationResults (
        std::vector<std::string> names_ = {},
        std::vector<int> npaths_ = {},
        std::vector<float> mean_ = {},
        std::vector<float> stddev_ = {},
        std::vector<float> skewness_ = {},
        std::vector<float> time_points_ = {},
        std::vector<int> time_steps_ = {},
        std::vector<Histogram> histograms_ = {}
    )
    : names (
        names_
    )
    , npaths (
        npaths_
    )
    , mean (
        mean_
    )
    , stddev (
        stddev_
    )
    , skewness (
        skewness_
    )
    , time_points (
        time_points_
    )
    , time_steps (
        time_steps_
    )
    , histograms (
        histograms_
    )
    {
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
        return true;
    }
    bool operator != (const EvaluationResults &other) const {return not(*this==other);}
};
void to_json(json &j, const EvaluationResults &obj) {
    j["names"] = obj.names;
    j["npaths"] = obj.npaths;
    j["mean"] = obj.mean;
    j["stddev"] = obj.stddev;
    j["skewness"] = obj.skewness;
    j["time_points"] = obj.time_points;
    j["time_steps"] = obj.time_steps;
    j["histograms"] = obj.histograms;
}

std::string to_json(const EvaluationResults &obj) {
    json j;
    to_json(j,obj);
    return j.dump();
}
void from_json(const json &j, EvaluationResults &obj) {
    j.at("names").get_to(obj.names);
    j.at("npaths").get_to(obj.npaths);
    j.at("mean").get_to(obj.mean);
    j.at("stddev").get_to(obj.stddev);
    j.at("skewness").get_to(obj.skewness);
    j.at("time_points").get_to(obj.time_points);
    j.at("time_steps").get_to(obj.time_steps);
    j.at("histograms").get_to(obj.histograms);
}
EvaluationResults EvaluationResults_from_json(const json &j) {
    EvaluationResults obj;
    from_json(j,obj);
    return obj;
}

class Parameter {
public:

    float value;
    float step;
    float min;
    float max;

    
    Parameter (
        float value_ = NAN,
        float step_ = NAN,
        float min_ = NAN,
        float max_ = NAN
    )
    : value (
        value_
    )
    , step (
        step_
    )
    , min (
        min_
    )
    , max (
        max_
    )
    {
    }

    bool operator == (const Parameter &other) const {
        if (value != other.value) return false;
        if (step != other.step) return false;
        if (min != other.min) return false;
        if (max != other.max) return false;
        return true;
    }
    bool operator != (const Parameter &other) const {return not(*this==other);}
};
void to_json(json &j, const Parameter &obj) {
    j["value"] = obj.value;
    j["step"] = obj.step;
    j["min"] = obj.min;
    j["max"] = obj.max;
}

std::string to_json(const Parameter &obj) {
    json j;
    to_json(j,obj);
    return j.dump();
}
void from_json(const json &j, Parameter &obj) {
    j.at("value").get_to(obj.value);
    j.at("step").get_to(obj.step);
    j.at("min").get_to(obj.min);
    j.at("max").get_to(obj.max);
}
Parameter Parameter_from_json(const json &j) {
    Parameter obj;
    from_json(j,obj);
    return obj;
}

class Model {
public:

    float TimeStart;
    int TimeSteps;
    int NumPaths;
    std::vector<Updater> updaters;
    std::vector<EvaluationPoint> evaluations;
    float RunTimeoutSeconds;
    int MemoryLimitKB;

    
    Model (
        float TimeStart_ = NAN,
        int TimeSteps_ = 0,
        int NumPaths_ = 0,
        std::vector<Updater> updaters_ = {},
        std::vector<EvaluationPoint> evaluations_ = {},
        float RunTimeoutSeconds_ = 1,
        int MemoryLimitKB_ = 1
    )
    : TimeStart (
        TimeStart_
    )
    , TimeSteps (
        TimeSteps_
    )
    , NumPaths (
        NumPaths_
    )
    , updaters (
        updaters_
    )
    , evaluations (
        evaluations_
    )
    , RunTimeoutSeconds (
        RunTimeoutSeconds_
    )
    , MemoryLimitKB (
        MemoryLimitKB_
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

    void Add (
        Updater updater
    )
    {
    }

    bool operator == (const Model &other) const {
        if (TimeStart != other.TimeStart) return false;
        if (TimeSteps != other.TimeSteps) return false;
        if (NumPaths != other.NumPaths) return false;
        if (updaters != other.updaters) return false;
        if (evaluations != other.evaluations) return false;
        if (RunTimeoutSeconds != other.RunTimeoutSeconds) return false;
        if (MemoryLimitKB != other.MemoryLimitKB) return false;
        return true;
    }
    bool operator != (const Model &other) const {return not(*this==other);}
};
void to_json(json &j, const Model &obj) {
    j["TimeStart"] = obj.TimeStart;
    j["TimeSteps"] = obj.TimeSteps;
    j["NumPaths"] = obj.NumPaths;
    j["updaters"] = obj.updaters;
    j["evaluations"] = obj.evaluations;
    j["RunTimeoutSeconds"] = obj.RunTimeoutSeconds;
    j["MemoryLimitKB"] = obj.MemoryLimitKB;
}

std::string to_json(const Model &obj) {
    json j;
    to_json(j,obj);
    return j.dump();
}
void from_json(const json &j, Model &obj) {
    j.at("TimeStart").get_to(obj.TimeStart);
    j.at("TimeSteps").get_to(obj.TimeSteps);
    j.at("NumPaths").get_to(obj.NumPaths);
    j.at("updaters").get_to(obj.updaters);
    j.at("evaluations").get_to(obj.evaluations);
    j.at("RunTimeoutSeconds").get_to(obj.RunTimeoutSeconds);
    j.at("MemoryLimitKB").get_to(obj.MemoryLimitKB);
}
Model Model_from_json(const json &j) {
    Model obj;
    from_json(j,obj);
    return obj;
}

