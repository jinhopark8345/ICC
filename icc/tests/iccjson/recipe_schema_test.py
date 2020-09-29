import jsonschema
import json
from jsonschema import validate

from json import *

def validateJson(jsonData, schema):
    try:
        validate(instance=jsonData, schema=schema)
    except jsonschema.exceptions.ValidationError as err:
        return False
    return True

def is_valid(json_data, schema):
    print("given json_data: {}".format(json_data))
    if validateJson(json_data, schema):
        print("Given JSON data is Valid")
    else:
        print("Given JSON data is InValid")


def make_recipe_info():
    direction = []
    direction.append(["green onion water",500, "g"])
    direction.append(["carrot", 700, "kg"])
    direction.append(["water", 500, "ml"])
    recipes = {}
    recipes['recipe'] = []
    recipes['recipe'].append({
        'name': 'rice cake',
        'like': 7,
        'ingredients': direction
    })

    recipes['recipe'].append({
        'name': 'curry',
        'like': 5,
        'ingredients': direction
    })

    return recipes

recipe_schema_path = '../json/recipe_schema.json'
recipe_schema = get_schema(recipe_schema_path)
recipes_info = make_recipe_info()

# recipe_info_temp = recipes['recipe'][0]
recipe_info_temp = recipes_info['recipe'][1]

print()
is_valid(recipe_info_temp, recipe_schema)
