import json
import os

def get_json(json_path):
    json_data = ""
    with open(json_path, 'r') as f:
        json_data = f.read()
    json_file = json.loads(json_data)
    return json_file

def get_schema(name_schema):
    cur_dir = os.path.dirname(os.path.realpath(__file__))
    recipe_schema_path = cur_dir + '/recipe_schema.json'
    user_ing_schema_path = cur_dir + '/user_ing_schema.json'
    ing_info_schema_path = cur_dir + '/ing_info_schema.json'

    switcher = {
        "recipe": get_json(recipe_schema_path),
        "user_ing" : get_json(user_ing_schema_path),
        "ing_info" : get_json(ing_info_schema_path)
    }
    
    return switcher.get(name_schema)

def get_test(test_name):
    cur_dir = os.path.dirname(os.path.realpath(__file__))
    recipe_test_path = cur_dir + '/recipe_test.json'
    user_ing_test_path = cur_dir + '/user_ing_test.json'
    ing_info_test_path = cur_dir + '/ing_info_test.json'

    switcher = {
        "recipe": get_json(recipe_test_path),
        "user_ing" : get_json(user_ing_test_path),
        "ing_info" : get_json(ing_info_test_path)
    }

    return switcher.get(test_name)

def get_data(name_json):
    cur_dir = os.path.dirname(os.path.realpath(__file__))

    recipe_path= cur_dir + '/recipe.json'
    user_ing_path= cur_dir + '/user_ing.json'
    ing_info_path = cur_dir +'/ing_info.json'

    switcher = {
        "recipe_json": get_json(recipe_path),
        "user_ing_json" : get_json(user_ing_path),
        "ing_info_json" : get_json(ing_info_path)
    }
    
    return switcher.get(name_json)
