import jsonschema
import json
from jsonschema import validate

ingredient_schema_path = './ingredient_store_schema.json'

with open(ingredient_schema_path, 'r') as f:
    schema_data = f.read()
ing_schema = json.loads(schema_data)

def validateJson(jsonData):
    try:
        validate(instance=jsonData, schema=ing_schema)
    except jsonschema.exceptions.ValidationError as err:
        return False
    return True

# Convert json to python object.

# valid data with all properties
jsonData = json.loads('{"name": "green onion", "store_method": "fridge", "expiration_duration": 3600, "image": "asdfklajsdfaj"}')

# valid data without image data
# jsonData = json.loads('{"name": "green onion", "store_method": "fridge", "expiration_duration": 3600}')

# invalid data / number is string
# jsonData = json.loads('{"name": "green onion", "store_method": "fridge", "expiration_duration": "3600"}')

# validate it
isValid = validateJson(jsonData)
if isValid:
    print(jsonData)
    print("Given JSON data is Valid")
else:
    print(jsonData)
    print("Given JSON data is InValid")

# # Convert json to python object.
# jsonData = json.loads('{"name": "jane doe", "rollnumber": 25, "marks": 72}')
# # validate it
# isValid = validateJson(jsonData)
# if isValid:
#     print(jsonData)
#     print("Given JSON data is Valid")
# else:
#     print(jsonData)
#     print("Given JSON data is InValid")
