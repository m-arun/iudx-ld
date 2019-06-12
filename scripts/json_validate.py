from jsonschema import validate
import json

schemaFile = "../base_schemas/iudx_resourceItem_context.json"
itemFile = "../ex_items/testItem.json"


schema = json.loads(schemaFile)
itemFile = json.loads(itemFile)

resolver = jsonschema.RefResolver('file://' +  , None)
