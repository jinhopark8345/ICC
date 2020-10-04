import pymongo
import datetime
import pprint

from pymongo import MongoClient

from iccjson.jconnect import *
from recommend.compare_recipe import *
from recommend.recommend_recipe import *


client = MongoClient()


db = client.test_database

# collection = db.test_collection

# print(collection)

# post = {"author": "Jinho",
#          "text": "Hello wolrd!",
#          "tags": ["mongodb", "python", "pymongo"],
#          "date": datetime.datetime.utcnow()}

# # print(post)

# posts = db.posts
# post_id = posts.insert_one(post).inserted_id
# # print(post_id)

# print(db.list_collection_names())

# # print(pprint.pprint(posts.find_one({"author": "Jinho"})))

# jinho_post = posts.find_one({"author": "Jinho"})
# print(jinho_post)

user_ings_data = get_data("user_ing")
recipes_data = get_data("recipe")
print(type(recipes_data))
print(type(recipes_data[0]))
print(type(user_ings_data))

# recipes = db.recipes
# recipe_id = recipes.insert_one(recipes_data)
