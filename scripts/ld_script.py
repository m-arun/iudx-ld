from pyld import jsonld
import json
import requests



itemFile = "./item2.json"
with open(itemFile, "r") as f:
    item = json.load(f)

context = {}
ctxt = item["@context"]
if( isinstance(ctxt, (list,))):
    for lnk in ctxt:
        r = requests.get(lnk)
        print(r.json())
        context.update(r.json()["@context"])
print(context)
    
#with open(itemFile, "r") as f:
#    item = json.load(f)
#
#
#doc = {k:v for k,v in item.items() if k not in "@context"}
#
#
#
#compacted = jsonld.compact(doc,context)
#print("Compacted")
#print(json.dumps(compacted, indent=2))
#print("\n\n")
#expanded = jsonld.expand(compacted)
#print("Expanded")
#print(json.dumps(expanded, indent=2))
#print("\n\n")
#flattened = jsonld.flatten(doc)
#print("Flattened")
#print(json.dumps(flattened, indent=2))
#print("\n\n")
#normalized = jsonld.normalize(
#    doc, {'algorithm': 'URDNA2015', 'format': 'application/n-quads'})
#print("Normalized")
#print(json.dumps(normalized, indent=2))
#print("\n\n")
