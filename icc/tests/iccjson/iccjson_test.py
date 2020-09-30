import jsonschema
import json
from jsonschema import validate

from iccjson.schema import *
#from iccjson.JSON_Link import *

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

def recipe_schema_test():
    recipe_schema = get_schema("recipe")
    recipes_info = make_recipe_info()
    recipe_info = recipes_info['recipe'][1]
    # is_valid(recipe_info_temp, recipe_schema)

    if validateJson(recipe_info, recipe_schema):
        print("recipe_schmea_test passed")
    else:
        print("recipe_schmea_test didn't passed")

    pass

def user_ingredient_schema_test():
    user_ing_schema = get_schema("user_ing")
    user_ing_infos = get_json("user_ing_json")
    user_ing_info = user_ing_infos['user_ingredient'][0]
    if validateJson(user_ing_info, user_ing_schema):
        print("user_ingredient_schema_test passed")
    else:
        print("user_ingredient_schema_test didn't passed")

    pass
def ingredient_info_schema_test():
    ing_info_schema = get_schema("ing_info")  
    ing_infos = get_json("ing_info_json")
    ing_info = ing_infos['ingredient_info'][0]
    print(len(ing_infos['ingredient_info']))

    for i in range ( len(ing_infos['ingredient_info']) ):
        ing_info = ing_infos['ingredient_info'][i]
        if validateJson(ing_info, ing_info_schema):
            print("user_ingredient_schema_test passed")
        else:
            print("array number =  " , i)
            print("user_ingredient_schema_test didn't passed")
        


    


    pass


def schema_test():
    recipe_schema_test()
    user_ingredient_schema_test()
    ingredient_info_schema_test()

