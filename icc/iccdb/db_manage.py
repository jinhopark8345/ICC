import pymongo
import datetime
import pprint

from pymongo import MongoClient
from pymongo import ReturnDocument

from iccjson.jconnect import get_schema, validateJson


class Icc_db:
  def __init__(self, db_name):
    self.client = MongoClient()
    self.db = self.client[db_name]
    self.user_ing = self.db.user_ing
    self.recipe = self.db.recipe
    self.ing_info = self.db.ing_info

  def add_ing_info(self, ing_info):
    """add ing to ing_info if it doesn't exist,
        if so, then update the ing

        Args:
            ing: ingredient to be added to user_ing
            ing_example = {"onion", "fridge", "1440"}
        Returns:
        """
    # check if the format is correct
    ing_info_schema = get_schema("ing_info")
    if not validateJson(ing_info, ing_info_schema):
      # temporary sol, need to change
      return -1

    # check if the ingredient exists on db already
    if self.ing_info.find_one({"name": ing_info["name"]}) == None:
      return self.ing_info.insert_one(ing_info)

    else:
      # ingredient already exist
      return -2

  def find_ing_info(self, ing_name):
    ing = self.ing_info.find_one({"name": ing_name})

    # return None if ing doesn't exist on DB
    return ing

  def update_ing_info(self, ing):
    pass

  def delete_ing_info(self, ing_name):
    return self.ing_info.delete_many({"name": ing_name})

  def add_user_ing(self, user_ing):
    # check if the format is correct
    user_info_schema = get_schema("user_ing")
    if not validateJson(user_ing, user_info_schema):
      # temporary sol, need to change
      return -1

    # check if the ingredient exists on db already
    if self.user_ing.find_one({"name": user_ing["name"]}) == None:
      return self.user_ing.insert_one(user_ing)
    else:
      # ingredient already exist
      return -2

  def find_user_ing(self, ing_name, returnID=True):
    if returnID == False:
      # find_one will find the object and return the object with id(default)
      ing = self.user_ing.find_one({"name": ing_name}, {"_id": False})
      return ing

    else:
      ing = self.user_ing.find_one({"name": ing_name})
      return ing

  def update_user_ing(self, ing):
    """update user_ing quantity if user has the ing,
        if not, then add the whole ing to user_ing

        Args:
            ing: ingredient to be added to user_ing
            ing_example = {"onion", 600, "g", "2020-10-07 13:34"}
        Returns:
        """

    # https://docs.mongodb.com/manual/reference/operator/update/
    # $inc is update operators
    # The *upsert* option can be used to create the document if it
    # doesn't already exist.  when ingredient is updated, _id doesn't
    # get added to the ingredient
    if (self.user_ing.find_one_and_update(
        {"name": ing["name"]},
        {"$inc": {
            "quantity": ing["quantity"]
        }},
        upsert=False,
    ) == None):

      # since find_one_and_update doesn't add other properties
      # than name and quantity, should insert whole new
      # ingreident to user_ing
      self.user_ing.insert_one(ing)

  # def find_all_user_ing(self, returnID=True):
  #   if returnID == False:
  #     # find_one will find the object and return the object with id(default)
  #     return self.user_ing.find({},{"_id": False})
  #   else:
  #     return self.user_ing.find({})

  def print_all_user_ing(self):
    # user_ing = self.user_ing.find({})
    for ing in self.user_ing.find({}):
      print(ing)

  def delete_user_ing(self, ing_name):
    self.user_ing.delete_one({"name": ing_name})
