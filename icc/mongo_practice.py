import pymongo
import datetime
import pprint

from pymongo import MongoClient

from iccjson.jconnect import *
from recommend.compare_recipe import *
from recommend.recommend_recipe import *

# user_ings_data = get_data("user_ing")
# recipes_data = get_data("recipe")

# print(type(recipes_data))
# print(type(recipes_data[0]))
# print(type(user_ings_data))


def make_ing(name, quantity, unit, date):
    return {
        "name": name,
        "quantity": quantity,
        "quantity_unit": unit,
        "store_time": date,
    }

client = MongoClient()
db = client.icc
user_ing = db.user_ing

ing5 = make_ing("onion", 500, "g", "2020-10-07 13:34")

def add_ing(ing, user_ing): # ing: ingredient json {}, user_ing: db.collection
    user_ing.insert_one(ing)

    # need to check if same name ingredient exist

    # no -> add

    # yes -> update quantity


def find_ing(ing_name, user_ing):
    ing = user_ing.find_one({'name': ing_name})
    return ing

# add_ing(ing5, user_ing)
output_ing = find_ing('onion', user_ing)
print(output_ing['quantity'])
