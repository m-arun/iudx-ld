from jsonschema import validate
import json

schemaFile = "https://raw.githubusercontent.com/rraks/iudx-ld/master/base_schemas/iudx_resourceItem_schema.json"
itemFile = "ex_items/testItem.json"


with open(itemFile, "r") as f:
    item = json.load(f)

try:
    validate(item, schemaFile)
except Exception as e:
    print(e)

