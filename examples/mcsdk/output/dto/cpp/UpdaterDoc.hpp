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
inline
void to_json(json &j, const UpdaterDoc &obj) try {
    j = json::object();
    j["name"] = obj.name;
    j["title"] = obj.title;
    j["doc_md"] = obj.doc_md;
    j["start"] = obj.start;
    j["nargs_min"] = obj.nargs_min;
    j["nrefs_min"] = obj.nrefs_min;
} catch (const std::exception &e) {
    std::throw_with_nested(std::runtime_error("void to_json(json &j, const UpdaterDoc &obj) exception"));
}

inline
std::string UpdaterDoc_to_json_string(const UpdaterDoc &obj) {
    json j;
    to_json(j,obj);
    return j.dump();
}
inline
void from_json(const json &j, UpdaterDoc &obj) try {
    j.at("name").get_to(obj.name);
    j.at("title").get_to(obj.title);
    j.at("doc_md").get_to(obj.doc_md);
    j.at("start").get_to(obj.start);
    j.at("nargs_min").get_to(obj.nargs_min);
    j.at("nrefs_min").get_to(obj.nrefs_min);
} catch (const std::exception &e) {
    std::throw_with_nested(std::runtime_error("void from_json(const json &j, UpdaterDoc &obj) exception"));
}
inline
UpdaterDoc UpdaterDoc_from_json(const json &j) {
    UpdaterDoc obj;
    from_json(j,obj);
    return obj;
}
} // namespace dto

