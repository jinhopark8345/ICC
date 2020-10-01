import jsonschema
import json
from jsonschema import validate

import unittest
from icc.iccjson.schema import *

def validateJson(jsonData, schema):
    try:
        validate(instance=jsonData, schema=schema)
    except jsonschema.exceptions.ValidationError as err:
        return False
    return True

def test_recipe_schema():
    recipe_schema = get_schema("recipe")
    recipes_test = get_test("recipe")
    recipe_test = recipes_test[0]

    assert validateJson(recipe_test, recipe_schema) == True

def test_user_ing_schema():
    user_ing_schema = get_schema("user_ing")
    user_ing_infos = get_test("user_ing")
    print(type(user_ing_infos))
    for i in range ( len(user_ing_infos) ):
        user_ing_info = user_ing_infos[i]
        assert validateJson(user_ing_info, user_ing_schema) == True

def test_ing_info_schema():
    ing_info_schema = get_schema("ing_info")
    ing_infos = get_test("ing_info")
    for i in range ( len(ing_infos) ):
        ing_info = ing_infos[i]
        assert validateJson(ing_info, ing_info_schema) == True
    
