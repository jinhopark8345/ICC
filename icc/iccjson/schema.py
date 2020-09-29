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
    ing_info_schema_path = './iccjson/ing_info_schema.json'

    switcher = {
        "recipe": find_schema(recipe_schema_path),
        "user_ingredient" : find_schema(user_ingredient_schema_path),
        "ing_info" : find_schema(ing_info_schema_path)
    }
    
    return switcher.get(name_schema)

