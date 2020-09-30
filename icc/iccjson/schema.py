import json
import os

def find_schema(schema_path):
    schema_data = ""
    with open(schema_path, 'r') as f:
        schema_data = f.read()
    schema = json.loads(schema_data)
    return schema

def get_schema(name_schema):

    recipe_schema_path = './iccjson/recipe_schema.json'
    user_ingredient_schema_path = './iccjson/user_ingredient_schema.json'
    ing_info_schema_path = './iccjson/ingredient_info_schema.json'

    switcher = {
        "recipe": find_schema(recipe_schema_path),
        "user_ing" : find_schema(user_ingredient_schema_path),
        "ing_info" : find_schema(ing_info_schema_path)
    }
    
    return switcher.get(name_schema)

def find_json(json_path):
    json_data = ""
    with open(json_path, 'r') as f:
        json_data = f.read()
    json_file = json.loads(json_data)
    return json_file

def get_json(name_json):
    #recipe_json_path = './iccjson/recipe_test.json'
    user_ingredient_json_path = './iccjson/user_ingredient.json'
    ing_info_json_path = './iccjson/ingredient_info.json'

    switcher = {
     #   "recipe_json": find_json(recipe_json_path),
        "user_ing_json" : find_json(user_ingredient_json_path),
        "ing_info_json" : find_json(ing_info_json_path)
    }
    
    return switcher.get(name_json)
# def find_test(test_path):
#     test_data = ""
#     with open(test_path, 'r') as f:
#         test_data = f.read()
#     test = json.loads(test_data)
#     return test

# def get_test(test_name):
#     recipe_test_path = './iccjson/recipe_test.json'
#     user_ingredient_test_path = './iccjson/user_ingredient_test.json'
#     ing_info_test_path = './iccjson/ingredient_info_test.json'

#     switcher = {
#         "recipe": find_test(recipe_test_path),
#         "user_ing" : find_test(user_ingredient_test_path),
#         "ing_info" : find_test(ing_info_test_path)
#     }

#     return switcher.get(test_name)
