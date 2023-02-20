// This is an automatically generated file.

#include <optional>
#include <string>
#include <vector>
#include <stdexcept>
#include <cmath>

#include <nlohmann/json.hpp>
using json = nlohmann::json;

class UpdaterDoc;
std::string UpdaterDoc_to_json_string(const UpdaterDoc &obj);
class UpdaterDoc {
public:

    std::string name;
    std::string title;
    std::string doc_md;
    std::string start;
    int nargs_min;
    int nrefs_min;

    
    UpdaterDoc (
        std::string name = "",
        std::string title = "",
        std::string doc_md = "",
        std::string start = "",
        int nargs_min = -88,
        int nrefs_min = -88
    )
    : name (
        name
    )
    , title (
        title
    )
    , doc_md (
        doc_md
    )
    , start (
        start
    )
    , nargs_min (
        nargs_min
    )
    , nrefs_min (
        nrefs_min
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
    std::string json (void) const {
        return UpdaterDoc_to_json_string(*this);
    }
};
void to_json(json &j, const UpdaterDoc &obj) {
    j["name"] = obj.name;
    j["title"] = obj.title;
    j["doc_md"] = obj.doc_md;
    j["start"] = obj.start;
    j["nargs_min"] = obj.nargs_min;
    j["nrefs_min"] = obj.nrefs_min;
}

std::string UpdaterDoc_to_json_string(const UpdaterDoc &obj) {
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

class UpdaterDto;
std::string UpdaterDto_to_json_string(const UpdaterDto &obj);
class UpdaterDto {
public:

    std::string name;
    std::optional<std::vector<int>> refs;
    std::optional<std::vector<float>> args;
    std::optional<float> start;

    
    UpdaterDto (
        std::string name = "",
        std::optional<std::vector<int>> refs = {},
        std::optional<std::vector<float>> args = {},
        std::optional<float> start = {}
    )
    : name (
        name
    )
    , refs (
        refs
    )
    , args (
        args
    )
    , start (
        start
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
    std::string json (void) const {
        return UpdaterDto_to_json_string(*this);
    }
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

std::string UpdaterDto_to_json_string(const UpdaterDto &obj) {
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
};
void to_json(json &j, const Updater &obj) {
    to_json(j,static_cast<const UpdaterDto &>(obj));
}

std::string Updater_to_json_string(const Updater &obj) {
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
};
void to_json(json &j, const IndependentGaussian &obj) {
    to_json(j,static_cast<const Updater &>(obj));
}

std::string IndependentGaussian_to_json_string(const IndependentGaussian &obj) {
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

class CorrelatedGaussian;
std::string CorrelatedGaussian_to_json_string(const CorrelatedGaussian &obj);
class CorrelatedGaussian: public Updater {
public:


    
    CorrelatedGaussian (
        float correlation = NAN,
        int state1 = -88,
        int state2 = -88,
        std::string title = ""
    )
    : Updater (
        "CorrelatedGaussian",
        {state1,state2},
        {correlation},
        {},
        title
    )
    {
    }

    bool operator == (const CorrelatedGaussian &other) const {
        if (Updater::operator != (other)) return false;
        return true;
    }
    bool operator != (const CorrelatedGaussian &other) const {return not(*this==other);}
    std::string json (void) const {
        return CorrelatedGaussian_to_json_string(*this);
    }
};
void to_json(json &j, const CorrelatedGaussian &obj) {
    to_json(j,static_cast<const Updater &>(obj));
}

std::string CorrelatedGaussian_to_json_string(const CorrelatedGaussian &obj) {
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

class BrownianMotion;
std::string BrownianMotion_to_json_string(const BrownianMotion &obj);
class BrownianMotion: public Updater {
public:


    
    BrownianMotion (
        float start = NAN,
        float drift = NAN,
        float diffusion = NAN,
        std::string title = ""
    )
    : Updater (
        "BrownianMotion",
        {},
        {drift,diffusion},
        start,
        title
    )
    {
    }

    bool operator == (const BrownianMotion &other) const {
        if (Updater::operator != (other)) return false;
        return true;
    }
    bool operator != (const BrownianMotion &other) const {return not(*this==other);}
    std::string json (void) const {
        return BrownianMotion_to_json_string(*this);
    }
};
void to_json(json &j, const BrownianMotion &obj) {
    to_json(j,static_cast<const Updater &>(obj));
}

std::string BrownianMotion_to_json_string(const BrownianMotion &obj) {
    json j;
    to_json(j,obj);
    return j.dump();
}
void from_json(const json &j, BrownianMotion &obj) {
    from_json(j,static_cast<Updater &>(obj));
}
BrownianMotion BrownianMotion_from_json(const json &j) {
    BrownianMotion obj;
    from_json(j,obj);
    return obj;
}

class BrownianMotionRef;
std::string BrownianMotionRef_to_json_string(const BrownianMotionRef &obj);
class BrownianMotionRef: public Updater {
public:


    
    BrownianMotionRef (
        float start = NAN,
        int drift = -88,
        int diffusion = -88,
        std::string title = ""
    )
    : Updater (
        "BrownianMotion",
        {drift,diffusion},
        {},
        start,
        title
    )
    {
    }

    bool operator == (const BrownianMotionRef &other) const {
        if (Updater::operator != (other)) return false;
        return true;
    }
    bool operator != (const BrownianMotionRef &other) const {return not(*this==other);}
    std::string json (void) const {
        return BrownianMotionRef_to_json_string(*this);
    }
};
void to_json(json &j, const BrownianMotionRef &obj) {
    to_json(j,static_cast<const Updater &>(obj));
}

std::string BrownianMotionRef_to_json_string(const BrownianMotionRef &obj) {
    json j;
    to_json(j,obj);
    return j.dump();
}
void from_json(const json &j, BrownianMotionRef &obj) {
    from_json(j,static_cast<Updater &>(obj));
}
BrownianMotionRef BrownianMotionRef_from_json(const json &j) {
    BrownianMotionRef obj;
    from_json(j,obj);
    return obj;
}

class GeometricalBrownianMotion;
std::string GeometricalBrownianMotion_to_json_string(const GeometricalBrownianMotion &obj);
class GeometricalBrownianMotion: public Updater {
public:


    
    GeometricalBrownianMotion (
        float start = NAN,
        float drift = NAN,
        float diffusion = NAN,
        std::string title = ""
    )
    : Updater (
        "GeometricalBrownianMotion",
        {},
        {drift,diffusion},
        start,
        title
    )
    {
    }

    bool operator == (const GeometricalBrownianMotion &other) const {
        if (Updater::operator != (other)) return false;
        return true;
    }
    bool operator != (const GeometricalBrownianMotion &other) const {return not(*this==other);}
    std::string json (void) const {
        return GeometricalBrownianMotion_to_json_string(*this);
    }
};
void to_json(json &j, const GeometricalBrownianMotion &obj) {
    to_json(j,static_cast<const Updater &>(obj));
}

std::string GeometricalBrownianMotion_to_json_string(const GeometricalBrownianMotion &obj) {
    json j;
    to_json(j,obj);
    return j.dump();
}
void from_json(const json &j, GeometricalBrownianMotion &obj) {
    from_json(j,static_cast<Updater &>(obj));
}
GeometricalBrownianMotion GeometricalBrownianMotion_from_json(const json &j) {
    GeometricalBrownianMotion obj;
    from_json(j,obj);
    return obj;
}

class GeometricalBrownianMotionRef;
std::string GeometricalBrownianMotionRef_to_json_string(const GeometricalBrownianMotionRef &obj);
class GeometricalBrownianMotionRef: public Updater {
public:


    
    GeometricalBrownianMotionRef (
        float start = NAN,
        int drift = -88,
        int diffusion = -88,
        std::string title = ""
    )
    : Updater (
        "GeometricalBrownianMotion",
        {drift,diffusion},
        {},
        start,
        title
    )
    {
    }

    bool operator == (const GeometricalBrownianMotionRef &other) const {
        if (Updater::operator != (other)) return false;
        return true;
    }
    bool operator != (const GeometricalBrownianMotionRef &other) const {return not(*this==other);}
    std::string json (void) const {
        return GeometricalBrownianMotionRef_to_json_string(*this);
    }
};
void to_json(json &j, const GeometricalBrownianMotionRef &obj) {
    to_json(j,static_cast<const Updater &>(obj));
}

std::string GeometricalBrownianMotionRef_to_json_string(const GeometricalBrownianMotionRef &obj) {
    json j;
    to_json(j,obj);
    return j.dump();
}
void from_json(const json &j, GeometricalBrownianMotionRef &obj) {
    from_json(j,static_cast<Updater &>(obj));
}
GeometricalBrownianMotionRef GeometricalBrownianMotionRef_from_json(const json &j) {
    GeometricalBrownianMotionRef obj;
    from_json(j,obj);
    return obj;
}

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
};
void to_json(json &j, const ZeroCouponBond &obj) {
    to_json(j,static_cast<const Updater &>(obj));
}

std::string ZeroCouponBond_to_json_string(const ZeroCouponBond &obj) {
    json j;
    to_json(j,obj);
    return j.dump();
}
void from_json(const json &j, ZeroCouponBond &obj) {
    from_json(j,static_cast<Updater &>(obj));
}
ZeroCouponBond ZeroCouponBond_from_json(const json &j) {
    ZeroCouponBond obj;
    from_json(j,obj);
    return obj;
}

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
void to_json(json &j, const Option &obj) {
    to_json(j,static_cast<const Updater &>(obj));
}

std::string Option_to_json_string(const Option &obj) {
    json j;
    to_json(j,obj);
    return j.dump();
}
void from_json(const json &j, Option &obj) {
    from_json(j,static_cast<Updater &>(obj));
}
Option Option_from_json(const json &j) {
    Option obj;
    from_json(j,obj);
    return obj;
}

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
void to_json(json &j, const Barrier &obj) {
    to_json(j,static_cast<const Updater &>(obj));
}

std::string Barrier_to_json_string(const Barrier &obj) {
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

class Multiplication;
std::string Multiplication_to_json_string(const Multiplication &obj);
class Multiplication: public Updater {
public:


    
    Multiplication (
        std::vector<int> refs = {},
        float factor = 1,
        std::string title = ""
    )
    : Updater (
        "Multiplication",
        refs,
        {factor},
        0,
        title
    )
    {
    }

    bool operator == (const Multiplication &other) const {
        if (Updater::operator != (other)) return false;
        return true;
    }
    bool operator != (const Multiplication &other) const {return not(*this==other);}
    std::string json (void) const {
        return Multiplication_to_json_string(*this);
    }
};
void to_json(json &j, const Multiplication &obj) {
    to_json(j,static_cast<const Updater &>(obj));
}

std::string Multiplication_to_json_string(const Multiplication &obj) {
    json j;
    to_json(j,obj);
    return j.dump();
}
void from_json(const json &j, Multiplication &obj) {
    from_json(j,static_cast<Updater &>(obj));
}
Multiplication Multiplication_from_json(const json &j) {
    Multiplication obj;
    from_json(j,obj);
    return obj;
}

class HistogramAxis;
std::string HistogramAxis_to_json_string(const HistogramAxis &obj);
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
    std::string json (void) const {
        return HistogramAxis_to_json_string(*this);
    }
};
void to_json(json &j, const HistogramAxis &obj) {
    j["state"] = obj.state;
    j["nbins"] = obj.nbins;
    j["min"] = obj.min;
    j["max"] = obj.max;
}

std::string HistogramAxis_to_json_string(const HistogramAxis &obj) {
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

class Histogram;
std::string Histogram_to_json_string(const Histogram &obj);
class Histogram {
public:

    HistogramAxis x;
    std::optional<HistogramAxis> y;

    
    Histogram (
        HistogramAxis x = HistogramAxis(),
        std::optional<HistogramAxis> y = {}
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
    std::string json (void) const {
        return Histogram_to_json_string(*this);
    }
};
void to_json(json &j, const Histogram &obj) {
    j["x"] = obj.x;
    if(obj.y.has_value())
        j["y"] = obj.y.value();
}

std::string Histogram_to_json_string(const Histogram &obj) {
    json j;
    to_json(j,obj);
    return j.dump();
}
void from_json(const json &j, Histogram &obj) {
    j.at("x").get_to(obj.x);
    if(auto it=j.find("y"); it!=j.end() and !it->is_null())
        obj.y = *it;
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

class EvaluationPoint;
std::string EvaluationPoint_to_json_string(const EvaluationPoint &obj);
class EvaluationPoint {
public:

    int state;
    float time;
    std::optional<float> value;
    std::optional<float> error;
    std::vector<Histogram> histograms;

    
    EvaluationPoint (
        int state = -88,
        float time = NAN,
        std::optional<float> value = {},
        std::optional<float> error = {},
        std::vector<Histogram> histograms = {}
    )
    : state (
        state
    )
    , time (
        time
    )
    , value (
        value
    )
    , error (
        error
    )
    , histograms (
        histograms
    )
    {
    }

    int GetState (
    ) const
    {
        
        return state;
        
    }

    int GetTime (
    ) const
    {
        
        return time;
        
    }

    float GetValue (
    ) const
    {
        
        if( not value.has_value() )
            throw std::invalid_argument("value");
        return value.value();
        
    }

    float GetError (
    ) const
    {
        
        if( not error.has_value() )
            throw std::invalid_argument("error");
        return error.value();
        
    }

    EvaluationPoint & Add (
        Histogram histogram
    )
    {
        
        histograms.push_back(histogram);
        return *this;
        
    }

    bool operator == (const EvaluationPoint &other) const {
        if (state != other.state) return false;
        if (time != other.time) return false;
        if (value != other.value) return false;
        if (error != other.error) return false;
        if (histograms != other.histograms) return false;
        return true;
    }
    bool operator != (const EvaluationPoint &other) const {return not(*this==other);}
    std::string json (void) const {
        return EvaluationPoint_to_json_string(*this);
    }
};
void to_json(json &j, const EvaluationPoint &obj) {
    j["state"] = obj.state;
    j["time"] = obj.time;
    if(obj.value.has_value())
        j["value"] = obj.value.value();
    if(obj.error.has_value())
        j["error"] = obj.error.value();
    j["histograms"] = obj.histograms;
}

std::string EvaluationPoint_to_json_string(const EvaluationPoint &obj) {
    json j;
    to_json(j,obj);
    return j.dump();
}
void from_json(const json &j, EvaluationPoint &obj) {
    j.at("state").get_to(obj.state);
    j.at("time").get_to(obj.time);
    if(auto it=j.find("value"); it!=j.end() and !it->is_null())
        obj.value = *it;
    if(auto it=j.find("error"); it!=j.end() and !it->is_null())
        obj.error = *it;
    j.at("histograms").get_to(obj.histograms);
}
EvaluationPoint EvaluationPoint_from_json(const json &j) {
    EvaluationPoint obj;
    from_json(j,obj);
    return obj;
}

class Parameter;
std::string Parameter_to_json_string(const Parameter &obj);
class Parameter {
public:

    float value;
    float step;
    float min;
    float max;

    
    Parameter (
        float value = NAN,
        float step = NAN,
        float min = NAN,
        float max = NAN
    )
    : value (
        value
    )
    , step (
        step
    )
    , min (
        min
    )
    , max (
        max
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
    std::string json (void) const {
        return Parameter_to_json_string(*this);
    }
};
void to_json(json &j, const Parameter &obj) {
    j["value"] = obj.value;
    j["step"] = obj.step;
    j["min"] = obj.min;
    j["max"] = obj.max;
}

std::string Parameter_to_json_string(const Parameter &obj) {
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

class Model;
std::string Model_to_json_string(const Model &obj);
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
        float TimeStart = NAN,
        int TimeSteps = 0,
        int NumPaths = 0,
        std::vector<Updater> updaters = {},
        std::vector<EvaluationPoint> evaluations = {},
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
        if(u.HasState())
            u._state = GetNumberOfStates()-1;
        return u;
        
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
    std::string json (void) const {
        return Model_to_json_string(*this);
    }
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

std::string Model_to_json_string(const Model &obj) {
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
void to_json(json &j, const Result &obj) {
    j["n"] = obj.n;
    j["mean"] = obj.mean;
    j["stddev"] = obj.stddev;
    j["skewness"] = obj.skewness;
}

std::string Result_to_json_string(const Result &obj) {
    json j;
    to_json(j,obj);
    return j.dump();
}
void from_json(const json &j, Result &obj) {
    j.at("n").get_to(obj.n);
    j.at("mean").get_to(obj.mean);
    j.at("stddev").get_to(obj.stddev);
    j.at("skewness").get_to(obj.skewness);
}
Result Result_from_json(const json &j) {
    Result obj;
    from_json(j,obj);
    return obj;
}

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
void to_json(json &j, const EvaluationResults &obj) {
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

std::string EvaluationResults_to_json_string(const EvaluationResults &obj) {
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
    if(auto it=j.find("model"); it!=j.end() and !it->is_null())
        obj.model = *it;
}
EvaluationResults EvaluationResults_from_json(const json &j) {
    EvaluationResults obj;
    from_json(j,obj);
    return obj;
}

