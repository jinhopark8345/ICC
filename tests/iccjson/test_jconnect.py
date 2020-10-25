import jsonschema
import json
from jsonschema import validate
from iccjson.jconnect import *


def test_ing_schema():
  '''
    should update this part
    using separate schema file for ingredient

    # ing_schema = get_schema("ing")
    # print(ing_schema)
    # ing = ing_test[0]
    # ing_schema = get_schema("ing")
    '''
  ing_test = get_test("ing")
  recipe_schema = get_schema("recipe")
  ing_schema = recipe_schema['properties']["ings"]['items'][0]
  # print(ing_schema)

  assert validateJson(ing_test[0], ing_schema) == True
  assert validateJson(ing_test[1], ing_schema) == False
  assert validateJson(ing_test[2], ing_schema) == False
  assert validateJson(ing_test[3], ing_schema) == False
  assert validateJson(ing_test[4], ing_schema) == True
  assert validateJson(ing_test[5], ing_schema) == False
  assert validateJson(ing_test[6], ing_schema) == True


def test_recipe_schema():
  recipe_schema = get_schema("recipe")
  recipes_test = get_test("recipe")
  recipe_test = recipes_test[0]

  assert validateJson(recipe_test, recipe_schema) == True


def test_user_ing_schema():
  user_ing_schema = get_schema("user_ing")
  user_ing_infos = get_test("user_ing")
  print(type(user_ing_infos))
  for i in range(len(user_ing_infos)):
    user_ing_info = user_ing_infos[i]
    assert validateJson(user_ing_info, user_ing_schema) == True


def test_ing_info_schema():
  ing_info_schema = get_schema("ing_info")
  ing_infos = get_test("ing_info")
  for i in range(len(ing_infos)):
    ing_info = ing_infos[i]
    assert validateJson(ing_info, ing_info_schema) == True
