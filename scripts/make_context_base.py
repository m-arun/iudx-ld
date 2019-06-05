import json

fl = "../base_schemas/iudx_base.json"
iudx_base_iri = "http://uri.iudx.org/json-ld"

doc = {}

with open(fl,"r") as f:
    doc = json.load(f)

props = doc["properties"]

context = {}

for prop in props:
    context[prop] = iudx_base_iri + "/" + prop

doc["@context"] = context
with open(fl+".jsonld", "w") as f:
    json.dump(doc, f, indent=4, sort_keys=True)
