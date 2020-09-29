import jsonschema
import json
from jsonschema import validate

ing_info_schema_path = '../json/ing_info_schema.json'

with open(ing_info_schema_path, 'r') as f:
    ing_info_schema_data = f.read()

ing_info_schema = json.loads(ing_info_schema_data)

def validateJson(jsonData, schema):
    try:
        validate(instance=jsonData, schema=schema)
    except jsonschema.exceptions.ValidationError as err:
        return False
    return True

# Convert json to python object.
# jsonData = json.loads('{"name": "green onion", "store_method": "akjsdlkfajsdfklj", "expiration_duration": 123, "image": "2020-06-20"}')

ing_info_path = '../json/ing_info.json'
with open(ing_info_path, 'r') as ff:
    ing_info_str = ff.read()
ing_info = json.loads(ing_info_str)
ing_info_temp = ing_info['ingredient_info'][1]

# print()
if validateJson(ing_info_temp, ing_info_schema):
    print(ing_info_temp)
    print("Given JSON data is Valid")
else:
    print(ing_info_temp)
    print("Given JSON data is InValid")
