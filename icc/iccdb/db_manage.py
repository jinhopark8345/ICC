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


class Icc_db:

    def __init__(self, db_name):
        # start db, if it's not on / should do it later
        self.client = MongoClient()
        self.db = self.client.icc

        self.user_ing = self.db.user_ing
        self.recipe = self.db.recipe
        self.ing_info = self.db.ing_info

    def add_user_ing(self, ing): # ing: ingredient json {}, user_ing: db.collection
        self.user_ing.insert_one(ing)
        # need to check if same name ingredient exist

        # no -> add

        # yes -> update quantity

    def find_user_ing(self, ing_name):
        ing = self.user_ing.find_one({'name': ing_name})
        return ing

# client = MongoClient()
# db = client.icc_test
# user_ing = db.user_ing


# add_ing(ing_example, user_ing)
# output_ing = find_ing('apple', user_ing)
# print(output_ing['quantity'])
# print(output_ing)

