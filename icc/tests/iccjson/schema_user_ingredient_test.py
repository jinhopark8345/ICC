import jsonschema
import json
from jsonschema import validate

def validateJson(jsonData, schema):
    try:
        validate(instance=jsonData, schema=schema)
    except jsonschema.exceptions.ValidationError as err:
        return False
    return True

user_ing_schema_path = '../json/user_ingredient_schema.json'
user_ing_path = '../json/user_ingredient.json'

with open(user_ing_schema_path, 'r') as f:
    user_info_schema_str = f.read()

user_ing_schema = json.loads(user_info_schema_str)

with open(user_ing_path, 'r') as ff:
    user_ing_str = ff.read()
# print(user_ing_str)

user_ing = json.loads(user_ing_str)

user_ing_temp = user_ing['user_ingredient'][0]

print()
if validateJson(user_ing_temp, user_ing_schema):
    print(user_ing_temp)
    print("Given JSON data is Valid")
else:
    print(user_ing_temp)
    print("Given JSON data is InValid")
