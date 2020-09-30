import json
import os

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
#user_ing_infos = get_json("user_ing_json")
#print(user_ing_infos)
