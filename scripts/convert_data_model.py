import json
import os
from os import listdir
from os.path import isfile, join


data_model = "../temp/data_models/environment/floodSensor/env_flood_climoPune_0.json"
dm_list = data_model.split("/")
dm_name = dm_list[-1]
path_to_dm = dm_list[data_model.index("data_models"):]
path_to_dm_folder = "".join(a+"/" for a in dm_list[:-1])
folder_path = "".join(a+"/" for a in path_to_dm)


core_context = "https://raw.githubusercontent.com/rraks/iudx-ld/master/base_schemas/core_context.json",
dm_url = "https://raw.githubusercontent.com/rraks/iudx-ld/master/data_models/" + folder_path + dm_name + "/properties/"

dm = {}
with open(data_model, "r") as f:
    dm = json.load(f)

props = dm["properties"]

context = {}
context["xsd"] = "http://www.w3.org/2001/XMLSchema#"
context["uo"] = "http://units.open.org/"



def makeOneOf(prop):
    tmpl = {}
    tmpl["oneOf"] = []
    tmpl["oneOf"].append({})
    tmpl["oneOf"][0]["type"] =  "object"
    tmpl["oneOf"][0]["properties"] = { "value": { "$ref": "#/properties/"+"xxx" } }
    tmpl["oneOf"].append({})
    tmpl["oneOf"][1]["type"] = "yyy" 
    tmpl["oneOf"][1]["$ref"] = "zzz" 
    tmpl["oneOf"][0]["properties"]["value"]["$ref"] = "#/properties/"+prop+"/valueSchema"
    tmpl["oneOf"][1]["type"] = props[prop]["type"]
    tmpl["oneOf"][1]["$ref"] = "#/properties/"+prop+"/valueSchema"
    return tmpl



props.pop("location")
props["deviceModelInfo"] = {"allOf": [{ "$ref":  "https://raw.githubusercontent.com/rraks/iudx-ld/master/base_schemas/miscSchemaOrgDefs.json#/definitions/product"}]}

for prop in props:
    if("type" in props[prop]):
        context[prop] = {"@id":dm_url + prop, "@type": "core:Property"}
        valueSchema = {}
        valueSchema["type"] = props[prop]["type"]
        if("minimum" in prop):
            valueSchema["minimum"] = props[prop]["minimum"]
        if("maximum" in props[prop]):
            valueSchema["maximum"] = props[prop]["maximum"]
        props[prop]["valueSchema"] = valueSchema
        oneOf = makeOneOf(prop)
        props[prop]["allOf"] = []
        props[prop]["allOf"].append({"$ref": "https://raw.githubusercontent.com/rraks/iudx-ld/master/base_schemas/core_defs.json#/definitions/Property"})
        props[prop].pop("type")
        props[prop].update(oneOf)



dm["@context"] = []
dm["@context"].append(core_context)
dm["@context"].append({})
dm["@context"][1] = context


print(path_to_dm_folder + dm_name[:-4] + "ld.json")
with open(path_to_dm_folder + dm_name[:-5] + "_ld.json", "w") as f:
    json.dump(dm, f, indent=4, sort_keys=True)


