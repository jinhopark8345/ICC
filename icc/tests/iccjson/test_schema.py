import jsonschema
import json
from jsonschema import validate

import unittest

import sys, os.path
icc_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
sys.path.insert(0, icc_dir)
from iccjson.schema import get_schema, get_test


def validateJson(jsonData, schema):
    try:
        validate(instance=jsonData, schema=schema)
    except jsonschema.exceptions.ValidationError as err:
        return False
    return True

def test_recipe_schema():
    recipe_schema = get_schema("recipe")
    recipes_test = get_test("recipe")
    recipe_test = recipes_test['recipe'][0]

    assert validateJson(recipe_test, recipe_schema) == True

def test_user_ing_schema():
    user_ing_schema = get_schema("user_ing")
    user_ing_infos = get_test("user_ing")
    user_ing_info = user_ing_infos['user_ing'][0]

    assert validateJson(user_ing_info, user_ing_schema) == True

def test_ing_info_schema():
    ing_info_schema = get_schema("ing_info")

    ing_infos = get_test("ing_info")
    assert validateJson(ing_infos['ing_info'][0], ing_info_schema) == False
    assert validateJson(ing_infos['ing_info'][1], ing_info_schema) == True

def test_schema():
    test_recipe_schema()
    test_user_ing_schema()
    test_ing_info_schema()

test_schema()
