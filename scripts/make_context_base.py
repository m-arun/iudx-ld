import json
import os
from os import listdir
from os.path import isfile, join


data_model = "../temp/data_models/environment/floodSensor/env_flood_climoPune_0.json"
dm_list = data_model.split("/")
dm_name = dm_list[-1]
path_to_dm = dm_list[data_model.index("data_models"):]
folder_path = "".join(a for a in path_to_dm)


core_context = "https://raw.githubusercontent.com/rraks/iudx-ld/master/base_schemas/core_context.json",
dm_url = "https://raw.githubusercontent.com/rraks/iudx-ld/master/data_models/" + folder_path + dm_name + "/properties/"

dm = {}
with open(data_model, "r") as f:
    dm = json.load(f)

props = dm["properties"]

context = {}
context["xsd"] = "http://www.w3.org/2001/XMLSchema#"
context["uo"] = "http://units.open.org/"


tmpl = {}
tmpl["oneOf"] = []
tmpl["oneOf"].append({})
tmpl["oneOf"][0]["allOf"] = [{"$ref": "https://raw.githubusercontent.com/rraks/iudx-ld/master/base_schemas/core_defs.json#/definitions/Property"}]
tmpl["oneOf"][0]["type"] =  "object"
tmpl["oneOf"][0]["properties"] = { "value": { "$ref": "#/properties/"+"xxx" } }
tmpl["oneOf"].append({})
tmpl["oneOf"][1]["allOf"] = [{"$ref": "https://raw.githubusercontent.com/rraks/iudx-ld/master/base_schemas/core_defs.json#/definitions/Property"}]
tmpl["oneOf"][1]["type"] = "yyy" 
tmpl["oneOf"][1]["$ref"] = "zzz" 




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
        tmpl["oneOf"][0]["properties"]["value"]["$ref"] = "#/properties/"+prop+"/valueSchema"
        tmpl["oneOf"][1]["type"] = props[prop]["type"]
        tmpl["oneOf"][1]["$ref"] = "#/properties/"+prop+"/valueSchema"
        props[prop].pop("type")
        props[prop].update(tmpl)



dm["@context"] = []
dm["@context"].append(core_context)
dm["@context"].append({})
dm["@context"][1] = context

print(json.dumps(dm, f, indent=4, sort_keys=True))

#
#with open(fl[:-4]+"json", "w") as f:
#    json.dump(doc, f, indent=4, sort_keys=True)
#
#
#doc = {}
#
#models = [os.path.abspath(name) for name in os.listdir(data_models) if os.path.isdir(name)]
#print(models)
#for model in models:
#    print("model \t", model)
#    onlyfiles = [f for f in listdir(model) if isfile(join(mypath, f))]

#
#
