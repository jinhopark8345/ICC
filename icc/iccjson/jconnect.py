import jsonschema
from jsonschema import validate
import json
import os


def validateJson(jsonData, schema):
    try:
        validate(instance=jsonData, schema=schema)
    except jsonschema.exceptions.ValidationError as err:
        return False
    return True


def get_json(json_path):
    json_data = ""
    with open(json_path, "r") as f:
        json_data = f.read()
    json_file = json.loads(json_data)
    return json_file


def get_schema(name_schema):
    cur_dir = os.path.dirname(os.path.realpath(__file__))
    recipe_schema_path = cur_dir + "/recipe_schema.json"
    user_ing_schema_path = cur_dir + "/user_ing_schema.json"
    ing_info_schema_path = cur_dir + "/ing_info_schema.json"
    ing_schema_path = cur_dir + "/ing_schema.json"

    switcher = {
        "ing": get_json(ing_schema_path),
        "recipe": get_json(recipe_schema_path),
        "user_ing": get_json(user_ing_schema_path),
        "ing_info": get_json(ing_info_schema_path),
    }

    return switcher.get(name_schema)


def get_test(test_name):
    cur_dir = os.path.dirname(os.path.realpath(__file__))
    recipe_test_path = cur_dir + "/recipe_test.json"
    user_ing_test_path = cur_dir + "/user_ing_test.json"
    ing_info_test_path = cur_dir + "/ing_info_test.json"
    ing_test_path = cur_dir + "/ing_test.json"

    switcher = {
        "ing": get_json(ing_test_path),
        "recipe": get_json(recipe_test_path),
        "user_ing": get_json(user_ing_test_path),
        "ing_info": get_json(ing_info_test_path),
    }

    return switcher.get(test_name)


def get_data(name_json):
    cur_dir = os.path.dirname(os.path.realpath(__file__))

    recipe_path = cur_dir + "/recipe.json"
    user_ing_path = cur_dir + "/user_ing.json"
    ing_info_path = cur_dir + "/ing_info.json"

    switcher = {
        "recipe": get_json(recipe_path),
        "user_ing": get_json(user_ing_path),
        "ing_info": get_json(ing_info_path),
    }

    return switcher.get(name_json)


def make_user_ing(name, quantity, unit, date):
    return {
        "name": name,
        "quantity": quantity,
        "quantity_unit": unit,
        "store_time": date,
    }


def make_ing_info(name, store_method, exp_dur):
    return {
        "name": name,
        "store_method": store_method,
        "expiration_duration": exp_dur
    }


def make_recipe(name, like, ings):
    return {"name": name, "like": like, "ings": ings}


def make_temp_recipes():
    return [{
        "name":
        "rice cake",
        "like":
        7,
        "ings": [{
            "name": "green onion",
            "quantity": 500,
            "quantity_unit": "g"
        }, {
            "name": "pepper",
            "quantity": 700,
            "quantity_unit": "kg"
        }, {
            "name": "water",
            "quantity": 500,
            "quantity_unit": "ml"
        }, {
            "name": "water2",
            "quantity": 500,
            "quantity_unit": "ml"
        }, {
            "name": "water3",
            "quantity": 477,
            "quantity_unit": "ml"
        }, {
            "name": "kimchi",
            "quantity": 359,
            "quantity_unit": "kg"
        }]
    }, {
        "name":
        "curry",
        "like":
        5,
        "ings": [{
            "name": "red pepper",
            "quantity": 500,
            "quantity_unit": "kg"
        }, {
            "name": "onion",
            "quantity": 700,
            "quantity_unit": "kg"
        }, {
            "name": "kimchi",
            "quantity": 20,
            "quantity_unit": "kg"
        }]
    }]
