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

client = MongoClient()


db = client.test_database2

posts = db.posts
post_data = {
    'title': 'Python and MongoDB',
    'content': 'PyMongo is fun, you guys',
    'author': 'Scott'
}
result = posts.insert_one(post_data)
print('One post: {0}'.format(result.inserted_id))

bills_post = posts.find_one({'author': 'Scott'})
print(bills_post)
