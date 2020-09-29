import jsonschema
import json
from jsonschema import validate

# ingredient_schema_path = './ingredient_store_schema.json'
ingredient_schema_path = './block.py'

with open(ingredient_schema_path, 'r') as f:
    schema_data = f.read()
ing_schema = json.loads(schema_data)
print(ing_schema)

# def validateJson(jsonData, schema):
#     try:
#         validate(instance=jsonData, schema=schema)
#     except jsonschema.exceptions.ValidationError as err:
#         return False
#     return True

# Convert json to python object.

# # valid data with all properties
# jsonData = json.loads('{"name": "green onion", "store_method": "fridge", "expiration_duration": 3600, "image": "asdfklajsdfaj"}')
# print(jsonData)

# # valid data without image data
# # jsonData = json.loads('{"name": "green onion", "store_method": "fridge", "expiration_duration": 3600}')

# # invalid data / number is string
# # jsonData = json.loads('{"name": "green onion", "store_method": "fridge", "expiration_duration": "3600"}')

# # validate it
# isValid = validateJson(jsonData, ing_schema)
# if isValid:
#     print(jsonData)
#     print("Given JSON data is Valid")
# else:
#     print(jsonData)
#     print("Given JSON data is InValid")
