import jsonschema
import json

schemaFile = "base_schemas/iudx_resourceItem_schema.json"
itemFile = "ex_items/testItem.json"


with open(itemFile, "r") as f:
    item = json.load(f)

with open(schemaFile, "r") as f:
    schema = json.load(f)

try:
    jsonschema.validate(item, schema)
    print("Valid item")
except jsonschema.exceptions.ValidationError as errV:
    print("Validation error")

except jsonschema.exceptions.SchemaError as errS:
 print("Schema Error Occured")
 print(errS.message)

