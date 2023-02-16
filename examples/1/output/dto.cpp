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
        std::vector<int> refs_ = {},
        std::vector<float> args_ = {},
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
    if(auto it=j.find("refs"); it!=j.end())
        obj.refs = *it;
    if(auto it=j.find("args"); it!=j.end())
        obj.args = *it;
    if(auto it=j.find("start"); it!=j.end())
        obj.start = *it;
}
UpdaterDto UpdaterDto_from_json(const json &j) {
    UpdaterDto obj;
    from_json(j,obj);
    return obj;
}

