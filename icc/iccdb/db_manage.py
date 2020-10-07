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
        # self.db = self.client.db_name
        self.db = self.client[db_name]

        self.user_ing = self.db.user_ing
        self.recipe = self.db.recipe
        self.ing_info = self.db.ing_info

    def update_user_ing(self, ing):
        # ing: ingredient json {}, user_ing: db.collection

        # https://docs.mongodb.com/manual/reference/operator/update/
        # $inc is update operators
        if self.user_ing.find_one_and_update(
            {'name': ing['name']}, \
                {'$inc': {'quantity':ing['quantity']}}, \
                upsert=True \
            ) == None:
            add_user_ing(ing)


    def add_user_ing(self, ing): # ing: ingredient json {}, user_ing: db.collection

        # add ing to user_ing collection if user doesn't have the ing
        if self.find_user_ing(ing) == None:
            self.user_ing.insert_one(ing)
        # update ing to user_ing collection if user already have the ing

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

