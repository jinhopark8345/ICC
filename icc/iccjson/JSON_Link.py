import json
import os

def find_json(json_path):
    json_data = ""
    with open(json_path, 'r') as f:
        json_data = f.read()
    json_file = json.loads(json_data)
    return json_file

def get_schema(name_json):

    recipe_json_path = './iccjson/user_recipe.json'
    user_ingredient_json_path = './iccjson/user_ingredient.json'
    ing_info_json_path = './iccjson/ingredient_info.json'

    switcher = {
        "recipe": find_schema(recipe_json_path),
        "user_ing" : find_schema(user_ingredient_json_path),
        "ing_info" : find_schema(ing_info_json_path)
    }
    
    return switcher.get(name_schema)
