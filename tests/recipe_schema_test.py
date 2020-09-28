import jsonschema
import json
from jsonschema import validate


def validateJson(jsonData, schema):
    try:
        validate(instance=jsonData, schema=schema)
    except jsonschema.exceptions.ValidationError as err:
        return False
    return True

recipe_schema_path = '../json/recipe_schema.json'

with open(recipe_schema_path, 'r') as f:
    recipe_schema_data = f.read()

recipe_schema = json.loads(recipe_schema_data)

# Convert json to python object.
direction = []
direction.append([12,"water water"])
direction.append([7,"water water water"])

# jsonData = json.loads('{"name": "rice cake", "like": 7, "ingredients": [1,"asdasd"]}')

data = {}
data['recipe'] = []
data['recipe'].append({
    'name': 'rice cake',
    'like': "7",
    'ingredients': direction
})

# print(data)

# ing_info_path = '../json/ing_info.json'
# with open(ing_info_path, 'r') as ff:
#     ing_info_str = ff.read()

# ing_info = json.loads(ing_info_str)
# ing_info_temp = ing_info['ingredient_info'][1]

print()
if validateJson(data, recipe_schema):
    print(data)
    print("Given JSON data is Valid")
else:
    print(data)
    print("Given JSON data is InValid")
