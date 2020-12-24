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


def make_recipe_ing(name, quantity, unit):
    return {"name": name, "quantity": quantity, "quantity_unit": unit}


def make_ing_info(name, store_method, exp_dur):
    return {
        "name": name,
        "store_method": store_method,
        "expiration_duration": exp_dur
    }


def make_recipe(name, like, ings):
    return {"name": name, "like": like, "ings": ings}


def make_temp_ing_info():
    return [{
        "name": "green onion",
        "store_method": "fridge",
        "expiration_duration": 60 * 24    
    }, {
        "name": "onion",
        "store_method": "room",
        "expiration_duration": 60 * 24 * 14    
    }, {
        "name": "pepper",
        "store_method": "fridge",
        "expiration_duration": 60 * 24 * 365    
    }, {
        "name": "red pepper",
        "store_method": "fridge",
        "expiration_duration": 60 * 24 * 14    
    }, {
        "name": "kimchi",
        "store_method": "fridge",
        "expiration_duration": 60 * 24 * 60    
    }, {
        "name": "egg",
        "store_method": "fridge",
        "expiration_duration": 60 * 24 * 40    
    }, {
        "name": "rice cake",
        "store_method": "fridge",
        "expiration_duration": 60 * 24 * 30    
    }, {
        "name": "garlic",
        "store_method": "fridge",
        "expiration_duration": 60 * 24 * 30
    }, {
        "name": "water",
        "store_method": "room",
        "expiration_duration": 60 * 24 * 30
    }, {
        "name": "beef",
        "store_method": "fridge",
        "expiration_duration": 60 * 24 * 10
    }, {
        "name": "mackerel",
        "store_method": "fridge",
        "expiration_duration": 60 * 24 * 5
    },{
        "name": "soy sauce",
        "store_method": "room",
        "expiration_duration": 60 * 24 * 100
    },{
        "name": "sugar",
        "store_method": "room",
        "expiration_duration": 60 * 24 * 100
    },{
        "name": "ground pepper",
        "store_method": "room",
        "expiration_duration": 60 * 24 * 100
    },{
        "name": "sesame oil",
        "store_method": "room",
        "expiration_duration": 60 * 24 * 100
    },{
        "name": "shiitake mushrooms",
        "store_method": "room",
        "expiration_duration": 60 * 24 * 5
    },{
        "name": "duck meat",
        "store_method": "fridge",
        "expiration_duration": 60 * 24 * 10
    },{
        "name": "olive oil",
        "store_method": "room",
        "expiration_duration": 60 * 24 * 100
    },{
        "name": "ginger",
        "store_method": "fridge",
        "expiration_duration": 60 * 24 * 50
    },{
        "name": "carrot",
        "store_method": "fridge",
        "expiration_duration": 60 * 24 * 10
    },{
        "name": "chicken meat",
        "store_method": "frozen",
        "expiration_duration": 60 * 24 * 10
    },{
        "name": "teriyaki sauce",
        "store_method": "fridge",
        "expiration_duration": 60 * 24 * 300
    },{
        "name": "ketchup",
        "store_method": "fridge",
        "expiration_duration": 60 * 24 * 900
    },{
        "name": "barbecue sauce",
        "store_method": "fridge",
        "expiration_duration": 60 * 24 * 300
    },{
        "name": "starch syrup",
        "store_method": "room",
        "expiration_duration": 60 * 24 * 500
    },{
        "name": "cooking oil",
        "store_method": "room",
        "expiration_duration": 60 * 24 * 500
    },{
        "name": "potato",
        "store_method": "room",
        "expiration_duration": 60 * 24 * 30
    }]



def make_temp_user_ing():
    return [{
        "name": "green_onion",
        "quantity": 100,
        "quantity_unit": "g",
        "store_time": "2020-09-27 11:43"
    }, {
        "name": "pepper",
        "quantity": 200,
        "quantity_unit": "g",
        "store_time": "2020-09-28 15:33"
    }, {
        "name": "onion",
        "quantity": 1000,
        "quantity_unit": "g",
        "store_time": "2020-09-28 15:33"
    }, {
        "name": "kimchi",
        "quantity": 400,
        "quantity_unit": "g",
        "store_time": "2020-09-28 15:33"
    }, {
        "name": "egg",
        "quantity": 500,
        "quantity_unit": "g",
        "store_time": "2020-09-28 15:33"
    }, {
        "name": "rice cake",
        "quantity": 500,
        "quantity_unit": "g",
        "store_time": "2020-09-28 15:33"
    }, {
        "name": "garlic",
        "quantity": 100,
        "quantity_unit": "g",
        "store_time": "2020-09-28 15:33"
    }, {
        "name": "beef",
        "quantity": 400,
        "quantity_unit": "g",
        "store_time": "2020-09-28 15:33"
    }, {
        "name": "red pepper",
        "quantity": 1000,
        "quantity_unit": "g",
        "store_time": "2020-09-28 15:33"
    },{
        "name": "carrot",
        "quantity": 600,
        "quantity_unit": "g",
        "store_time": "2020-09-28 15:33"
    },{
        "name": "sugar",
        "quantity": 400,
        "quantity_unit": "g",
        "store_time": "2020-09-28 15:33"
    },{
        "name": "beef",
        "quantity": 1800,
        "quantity_unit": "g",
        "store_time": "2020-09-28 15:33"
    },{
        "name": "potato",
        "quantity": 1000,
        "quantity_unit": "g",
        "store_time": "2020-09-28 15:33"
    }]


def make_temp_recipe():
    return [{
        "name":
        "rice cake soup",
        "like":
        7,
        "ings": [{
            "name": "green onion",
            "quantity": 500,
            "quantity_unit": "g"
        }, {
            "name": "pepper",
            "quantity": 700,
            "quantity_unit": "g"
        }, {
            "name": "water",
            "quantity": 500,
            "quantity_unit": "ml"
        }, {
            "name": "rice cake",
            "quantity": 200,
            "quantity_unit": "g"
        }, {
            "name": "egg",
            "quantity": 100,
            "quantity_unit": "g"
        }]
    }, {
        "name":
        "curry",
        "like":
        5,
        "ings": [{
            "name": "red pepper",
            "quantity": 20,
            "quantity_unit": "g"
        }, {
            "name": "onion",
            "quantity": 200,
            "quantity_unit": "g"
        }, {
            "name": "potato",
            "quantity": 300,
            "quantity_unit": "g"
        },{
            "name": "carrot",
            "quantity": 150,
            "quantity_unit": "g"
        }]
    }, {
        "name":
        "kimchi stew",
        "like":
        4,
        "ings": [{
            "name": "red pepper",
            "quantity": 20,
            "quantity_unit": "g"
        }, {
            "name": "onion",
            "quantity": 200,
            "quantity_unit": "g"
        }, {
            "name": "kimchi",
            "quantity": 20,
            "quantity_unit": "g"
        }, {
            "name": "sugar",
            "quantity": 20,
            "quantity_unit": "g"
        }, {
            "name": "soup soy sauce",
            "quantity": 20,
            "quantity_unit": "g"
        }, {
            "name": "pork",
            "quantity": 150,
            "quantity_unit": "g"
        }]
    }, {
        "name":
        "doenjang-jjigae",
        "like":
        9,
        "ings": [{
            "name": "red pepper",
            "quantity": 20,
            "quantity_unit": "g"
        }, {
            "name": "onion",
            "quantity": 200,
            "quantity_unit": "g"
        }, {
            "name": "sugar",
            "quantity": 10,
            "quantity_unit": "g"
        }, {
            "name": "beef",
            "quantity": 50,
            "quantity_unit": "g"
        }, {
            "name": "Doenjang",
            "quantity": 40,
            "quantity_unit": "g"
        }, {
            "name": "water",
            "quantity": 300,
            "quantity_unit": "ml"
        }]
    }, {
        "name":
        "grilled mackerel",
        "like":
        7,
        "ings": [{
            "name": "mackerel",
            "quantity": 220,
            "quantity_unit": "g"
        }, {
            "name": "soy sauce",
            "quantity": 10,
            "quantity_unit": "g"
        }, {
            "name": "onion",
            "quantity": 10,
            "quantity_unit": "g"
        }, {
            "name": "garlic",
            "quantity": 3,
            "quantity_unit": "g"
        }, {
            "name": "sugar",
            "quantity": 4,
            "quantity_unit": "g"
        }, {
            "name": "sesame oil",
            "quantity": 3,
            "quantity_unit": "ml"
        }, {
            "name": "pepper",
            "quantity": 0.5,
            "quantity_unit": "g"
        }, {
            "name": "salt",
            "quantity": 3,
            "quantity_unit": "g"
        }]
    }, {
        "name":
        "beef bulgogi",
        "like":
        10,
        "ings": [{
            "name": "beef",
            "quantity": 170,
            "quantity_unit": "g"
        }, {
            "name": "green onion",
            "quantity": 45,
            "quantity_unit": "g"
        }, {
            "name": "onion",
            "quantity": 12,
            "quantity_unit": "g"
        }, {
            "name": "shiitake mushroom",
            "quantity": 6,
            "quantity_unit": "g"
        }, {
            "name": "carrot",
            "quantity": 5,
            "quantity_unit": "g"
        }]
    }, {
        "name":
        "roast duck",
        "like":
        9,
        "ings": [{
            "name": "duck meat",
            "quantity": 220,
            "quantity_unit": "g"
        }, {
            "name": "salt",
            "quantity": 3,
            "quantity_unit": "g"
        }, {
            "name": "pepper",
            "quantity": 1,
            "quantity_unit": "g"
        }, {
            "name": "olive oil",
            "quantity": 3,
            "quantity_unit": "g"
        }, {
            "name": "Doenjang",
            "quantity": 40,
            "quantity_unit": "g"
        }, {
            "name": "water",
            "quantity": 300,
            "quantity_unit": "ml"
        }]
    }, {
        "name":
        "chicken teriyaki",
        "like":
        5,
        "ings": [{
            "name": "chicken meat",
            "quantity": 200,
            "quantity_unit": "g"
        }, {
            "name": "rice cake",
            "quantity": 42,
            "quantity_unit": "g"
        }, {
            "name": "potato",
            "quantity": 33,
            "quantity_unit": "g"
        }, {
            "name": "carrot",
            "quantity": 33,
            "quantity_unit": "g"
        }, {
            "name": "onion",
            "quantity": 5,
            "quantity_unit": "g"
        }, {
            "name": "green onion",
            "quantity": 5,
            "quantity_unit": "g"
        }, {
            "name": "cooking oil",
            "quantity": 3,
            "quantity_unit": "ml"
        }]
    }]

