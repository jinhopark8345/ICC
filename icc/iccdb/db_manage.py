import pymongo
import datetime

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

    def add_recipe(self, recipe):
        """add recipe to db.recipe if it doesn't exist,
        if so, then update the recipe

        Args:
            ing: ingredient to be added to user_ing
            ing_example = {"onion", "fridge", "1440"}
        Returns:
        """
        # check if the format is correct
        recipe_schema = get_schema("recipe")
        if not validateJson(recipe, recipe_schema):
            # temporary sol, need to change
            return -1

        # check if the recipe exists on db already
        if self.recipe.find_one({"name": recipe["name"]}) == None:
            return self.recipe.insert_one(recipe)

        # recipe already exist
        else:
            return -2

    def delete_recipe(self, recipe_name):
        return self.recipe.delete_many({"name": recipe_name})

    def replace_recipe_ings(self, recipe):
        """
        1. update like
        2. update ings
            1. add ing
            2. delete ing
            3. update ing - update quantity
        """
        return self.recipe.find_one_and_update({"name": recipe["name"]},
                                        {"$set": {
                                            "ings": recipe["ings"]
                                        }},
                                        upsert=False)

    def replace_recipe_like(self, recipe):
        """
        1. update like
        2. update ings
            1. add ing
            2. delete ing
            3. update ing - update quantity
        """
        return self.recipe.find_one_and_update({"name": recipe["name"]},
                                        {"$set": {
                                            "like": recipe["like"]
                                        }},
                                        upsert=False)

    def update_recipe_like(self, recipe_name, like=1, replace_flag=False):

        recipe = self.find_recipe(recipe_name)

        if not replace_flag:
            # like
            recipe["like"] += like
        # replace the like value
        else:
            recipe["like"] = like

        self.replace_recipe_like(recipe)

    def add_recipe_ing(self, recipe_name, ing):
        # 2. update ings - add ing
        recipe = self.find_recipe(recipe_name)

        ### Next SAIDS: need to add schema test
        recipe['ings'].append(ing)

        self.replace_recipe_ing(recipe)

    def delete_recipe_ing(self, recipe_name, ing_name):
        # 2. update ings - delete ing
        recipe = self.find_recipe(recipe_name)
        recipe['ings'] = [
            ing for ing in recipe['ings'] if ing["name"] != ing_name
        ]

        self.replace_recipe_ings(recipe)

    def update_recipe_ing_quantity(self, recipe_name, ing, replace_flag=False):
        # 2. update ing - update quantity

        ### Next SAIDS: need to add schema test

        recipe = self.find_recipe(recipe_name)
        for db_ing in recipe['ings']:
            if db_ing["name"] == ing["name"]:
                if not replace_flag:
                    db_ing["quantity"] += ing["quantity"]
                else:
                    db_ing["quantity"] = ing["quantity"]

        self.replace_recipe_ings(recipe)

        ############################################
        ############################################
        ############################################
        ############################################
        ############################################
        ############################################

    def find_ing_info(self, ing_name):
        ing = self.ing_info.find_one({"name": ing_name})

        # return None if ing doesn't exist on DB
        return ing

    def find_user_ing(self, ing_name, returnID=True):
        if returnID == False:
            # find_one will find the object and return the object with id(default)
            ing = self.user_ing.find_one({"name": ing_name}, {"_id": False})
            return ing

        else:
            ing = self.user_ing.find_one({"name": ing_name})
            return ing

    def find_recipe(self, recipe_name, returnID=True):
        if returnID == False:
            # find_one will find the object and return the object with id(default)
            recipe = self.recipe.find_one({"name": recipe_name},
                                          {"_id": False})
            return recipe
        else:
            recipe = self.recipe.find_one({"name": recipe_name})
            return recipe
