import json


itemPath = "../temp/data_models/environment/floodSensor/examples/exItem_env_flood_climoPune_0.json"
itemNameList = itemPath.split("/")
itemName = itemNameList[-1]
path_to_item = itemNameList[itemNameList.index("examples"):]


resourceItemSchemaPath = "../base_schemas/resourceItem_schema.json"

item = {}
with open(itemPath,"r") as f:
    item = json.load(f)

schema = {}
with open(resourceItemSchemaPath,"r") as f:
    schema = json.load(f)

def mkProperty(prop):
    temp = {}
    temp["type"] = "Property" 
    temp["value"] = prop
    return temp

def mkRelationship(rel):
    temp = {}
    temp["type"] = "Relationship" 
    temp["object"] = rel
    return temp

def mkTimeProperty(prop):
    temp = {}
    temp["type"] = "TimeProperty" 
    temp["value"] = prop
    return temp

def mkLocation(prop):
    temp = {}
    temp["type"] = "GeoProperty"
    temp["value"] = {}
    temp["value"]["type"] = "Point"
    temp["value"]["value"] = [prop["latitude"], prop["longitude"]]
    return temp


item["@id"] = item["id"]
item.pop("id")

t = item["tags"]
item["tags"] = mkProperty(t)

item["location"] = mkLocation(item["location"])

item["itemType"] = mkProperty("resourceItem" )
item.pop("__itemType")

item["status"] = mkProperty(item["__itemStatus"])
item.pop("__itemStatus")

item["createdAt"] = mkTimeProperty(item["__createdAt"])
item.pop("__createdAt")

item["accessObjectURL"] = mkRelationship(item["accessInformation"][0]["accessSchema"])
item["resourceServer"] = mkRelationship("iudx_iri:pscdcl_server")

item["resourceId"] = {}
item["resourceId"] = mkProperty(item["accessInformation"][0]["accessVariables"]["resourceId"])

item["accessObjectVariables"] = {}
item["accessObjectVariables"]["type"] = "Property"
item["accessObjectVariables"]["value"] = {}
item["accessObjectVariables"]["value"]["ip"] = item["accessInformation"][0]["accessVariables"]["resourceServerId"][:-4]
item["accessObjectVariables"]["value"]["port"] = item["accessInformation"][0]["accessVariables"]["resourceServerId"][-3:]
item["accessObjectVariables"]["value"]["resourceClass"] = item["accessInformation"][0]["accessVariables"]["resourceClass"]
item["accessObjectVariables"]["value"]["NAME"] = item["NAME"]
item.pop("accessInformation")


dm_fields = list( set(item.keys()) - set(schema.keys()) )

for dmField in dm_fields:
    item[dmField] = mkProperty(item[dmField])

print(json.dumps(item, f, indent=4))
#with open(path_to_dm_folder + dm_name[:-5] + "_ld.json", "w") as f:
#    json.dump(dm, f, indent=4, sort_keys=true)



