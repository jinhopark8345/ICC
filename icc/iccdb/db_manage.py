import pymongo
import datetime

from pymongo import MongoClient
from pymongo import ReturnDocument
from iccjson.jconnect import *
# from recommend.compare_recipe import get_need_ings


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

    def add_temp_user_ing(self):
        # clean db
        self.db.drop_collection("user_ing")
        user_ings = make_temp_user_ing()

        for user_ing in user_ings:
            # print(recipe)
            rtv = self.add_user_ing(user_ing)
            if rtv == -1 or rtv == -2:
                print("add_recipe error code : {}".format(rtv))

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

    def print_user_ing(self):
        # user_ing = self.user_ing.find({})
        for ing in self.user_ing.find({}):
            print(ing)

    def delete_user_ing(self, ing_name):
        self.user_ing.delete_one({"name": ing_name})

    """
    recipe manipulation methods

    1. add recipe:
        - add_recipe
    2. delete recipe:
        - delete_recipe
    3. recipe modification ( recipe has 'ings' and 'like')
        - replace_recipe_ings
        - replace_recipe_like

        // like
        - update_recipe_like: last function / using replace_recipe_ings

        // ing(s)
        - add_recipe_ing : add ing to recipe / using replace_recipe_ings
        - delete_recipe_ing : delete ing from recipe/ using replace_recipe_ings
        - update_recipe_ing: / using replace_recipe_ings
    """


    def add_recipe(self, recipe):
        """add recipe to db.recipe if it doesn't exist in database,
        if so, then update the recipe

        Args:
           recipe: type: dict. It include recpie_name, like, ings_name, ings_quantity_unit, ings_quantity.
           recipe_example :
           {
            "name":
            "rice cake soup",
            "like":
            7,
            "ings": [{
                "name": "green onion",
                "quantity": 500,
                "quantity_unit": "g"
            }]
            }
        Returns:
            -1 : output is an integer -1, when the format does not match the specific schema.
            -2 : output is an integer -2, when recipe to add already exist in dbMongo of recpies.
            "recipe" : output is recipe to add. type is dict 
            
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
        """delete one recipe to db.recipe,

        Args:
            recipe_name: type is string.
            
        Returns:
        """
        return self.recipe.delete_many({"name": recipe_name})

    def replace_recipe_ings(self, recipe):
        """ replace existing ing in recipe with new ing.  
        Args:
            recipe: type is dict. It include recpie_name, like, ings_name, ings_quantity_unit, ings_quantity.
            recipe_example :
           {
            "name":
            "rice cake soup",
            "like":
            7,
            "ings": [{
                "name": "green onion",
                "quantity": 500,
                "quantity_unit": "g"
            }]
            }
        Returns:
 
        """
        return self.recipe.find_one_and_update(
            {"name": recipe["name"]}, {"$set": {
                "ings": recipe["ings"]
            }},
            upsert=False)

    def replace_recipe_like(self, recipe):
        """ replace existing like in recipe with new like.
            
        Args:
            replace existing ing in recipe with new ing.
        Returns:
 
        """
        return self.recipe.find_one_and_update(
            {"name": recipe["name"]}, {"$set": {
                "like": recipe["like"]
            }},
            upsert=False)

    def update_recipe_like(self, recipe_name, like=1, replace_flag=False):
        """update value of like in recipe when replace_flag is False.
        when replace_flag is True, replace value of like in recipe with value of like as args.
        
        Args:
            recipe_name: type is string.
            like: type is integer.
            replace_flag: Optional; 
            
        Returns:   
 
        """
        recipe = self.find_recipe(recipe_name)

        if not replace_flag:
            # like
            recipe["like"] += like
        # replace the like value
        else:
            recipe["like"] = like

        self.replace_recipe_like(recipe)

    def add_recipe_ing(self, recipe_name, ing):
        """add ing in ings of recipe to db.recipe
        
        Args:
            recipe_name: type is string.
            ing: type is dict. ingredient to be added to ing in recipe.
            ing_example = {"onion", "fridge", "1440"}
            
        Returns:   
 
        """
        # need to check recipe ing schema
        recipe = self.find_recipe(recipe_name)

        ### Next SAIDS: need to add schema test
        recipe['ings'].append(ing)

        self.replace_recipe_ings(recipe)

    def delete_recipe_ing(self, recipe_name, ing_name):
        """delete ing in ings of recipe to db.recipe
        
        Args:
            recipe_name: type is string.
            ing_name: type is string. ingredient to be deleted to ing in ings of recipe.
        Returns:   
 
        """
        # 2. update ings - delete ing
        recipe = self.find_recipe(recipe_name)
        recipe['ings'] = [ 
            ing for ing in recipe['ings'] if ing["name"] != ing_name
        ]

        self.replace_recipe_ings(recipe)

    def update_recipe_ing(self, recipe_name, ing, replace_flag=False):
        """update value of ing_quantity in ing of recipe when replace_flag is False.
        when replace_flag is True, replace value of ing_quantity in ing of recipe with value of ing as args.
        
        Args:
            recipe_name: type is string.
            ing: type is dict.
            replace_flag: Optional; 
            
        Returns:   
 
        """
        # need to check recipe ing schema

        recipe = self.find_recipe(recipe_name)
        for db_ing in recipe['ings']:
            if db_ing["name"] == ing["name"]:
                if not replace_flag:
                    db_ing["quantity"] += ing["quantity"]
                else:
                    db_ing["quantity"] = ing["quantity"]

        self.replace_recipe_ings(recipe)
        
    def find_ing_info(self, ing_name):
        """find ing_info in db.ing_info
        
        Args:
            ing_name: type is string.
        Returns:
            ing_info: type is dict.  
        """
        ing_info = self.ing_info.find_one({"name": ing_name})

        # return None if ing doesn't exist on DB
        return ing_info

    def find_user_ing(self, ing_name, returnID=True):
        """find user_ing in db.user_ing.
        if returnID is True,print ID. else, not print ID.
        
        Args:
            ing_name: type is string.
            returnID: optional;
        Returns:
            ing: type is dict.  
        """
        if returnID == False:
            # find_one will find the object and return the object with id(default)
            ing = self.user_ing.find_one({"name": ing_name}, {"_id": False})
            return ing

        else:
            ing = self.user_ing.find_one({"name": ing_name})
            return ing

    def find_recipe(self, recipe_name, returnID=True):
        """find recipe in db.recipe.
        if returnID is True, print ID. else, not print ID.
        
        Args:
            recipe_name: type is string.
            returnID: optional;
        Returns:
            recipe: type is dict.  
        """
        if returnID == False:
            # find_one will find the object and return the object with id(default)
            recipe = self.recipe.find_one({"name": recipe_name},
                                          {"_id": False})
            return recipe
        else:
            recipe = self.recipe.find_one({"name": recipe_name})
            return recipe

    def find_recipes(self, returnID=True):
        """find all recipes in db.recipe.
        if returnID is True, print ID. else, not print ID.
        
        Args:
            returnID: optional;
        Returns:
            recipe: type is dict.  
        """
        cursor = self.recipe  # choosing the collection you need
        recipes = []

        if returnID == False:
            for recipe in cursor.find({}, {"_id": False}):
                recipes.append(recipe)
        else:
            for recipe in cursor.find({}):
                recipes.append(recipe)

        return recipes

    def find_recipe_ing(self, recipe_name, ing_name, returnID=True):
        """find ing of recipe in db.recipe.
        if returnID is True, print ID. else, not print ID.
        
        Args:
            returnID: optional;
        Returns:
            ing: type is dict.
        """
        if returnID == False:
            # find_one will find the object and return the object with id(default)
            recipe = self.recipe.find_one({"name": recipe_name},
                                          {"_id": False})
            for ing in recipe["ings"]:
                if ing["name"] == ing_name:
                    return ing
        else:
            recipe = self.recipe.find_one({"name": recipe_name})
            for ing in recipe["ings"]:
                if ing["name"] == ing_name:
                    return ing

    def find_user_ings(self, returnID=True):
        """find all user_ings in db.user_ing.
        if returnID is True, print ID. else, not print ID.
        
        Args:
            returnID: optional;
        Returns:
            ing_info: tpye is dict.
        """
        user_ings = []
        if returnID == False:
            for user_ing in self.user_ing.find({}, {"_id": False}):
                user_ings.append(user_ing)
        else:
            for user_ing in self.user_ing.find({}):
                user_ings.append(user_ing)
        return user_ings

    def find_ing_infos(self, returnID=False):
        """find all ing_infos in db.ing_info.
        if returnID is True, print ID. else, not print ID.
        
        Args:
            returnID: optional;
        Returns:
            ing_info: tpye is dict.
        """
    
        ing_infos = []
        if returnID == False:
            for ing_info in self.ing_info.find({}, {"_id": False}):
                ing_infos.append(ing_info)
        else:
            for ing_info in self.ing_info.find({}):
                ing_infos.append(ing_info)
        return ing_infos

    def add_temp_recipe(self):
        self.db.drop_collection("recipe")
    
        recipes = make_temp_recipe()
        for recipe in recipes:
            # print(recipe)
            temp = self.add_recipe(recipe)
            if temp == -1 or temp == -2:
                print("add_recipe error code : {}", temp)

    def add_temp_ing_info(self):
        # clean db
        self.db.drop_collection("ing_info")
        ing_infos = make_temp_ing_info()

        for ing_info in ing_infos:
            # print(recipe)
            rtv = self.add_ing_info(ing_info)
            if rtv == -1 or rtv == -2:
                print("add_recipe error code : {}".format(rtv))

