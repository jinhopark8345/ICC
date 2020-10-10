import pymongo
import datetime
import pprint


from pymongo import MongoClient
from pymongo import ReturnDocument


class Icc_db:
    def __init__(self, db_name):
        # start db, if it's not on / should do it later
        self.client = MongoClient()
        # self.db = self.client.db_name
        self.db = self.client[db_name]

        self.user_ing = self.db.user_ing
        self.recipe = self.db.recipe
        self.ing_info = self.db.ing_info

    def get_db(self):
        return self.db

    def get_user_ing(self):
        return self.user_ing

    def get_recipe(self):
        return self.recipe

    def get_ing_info(self):
        return self.ing_info

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
        # The *upsert* option can be used to create the document if it doesn't
        # already exist.
        # self.get_user_ing().find_one_and_update(
        #     {"name": ing["name"]},
        #     {"$inc": {"quantity": ing["quantity"]}},
        #     {"quantity_unit": ing["quantity_unit"]},
        #     {"store_time": ing["store_time"]},
        #     upsert=True,
        # )

        if (
            self.get_user_ing().find_one_and_update(
                {"name": ing["name"]},
                {"$inc": {"quantity": ing["quantity"]}},
                upsert=False,
            )
            == None
        ):
            # since find_one_and_update doesn't add other properties
            # than name and quantity, should insert whole new
            # ingreident to user_ing
            self.get_user_ing().insert_one(ing)

    def find_user_ing(self, ing_name, returnID=True):
        if returnID == False:
            ing = self.user_ing.find_one({"name": ing_name}, {"_id": False})
            return ing
        else:
            ing = self.user_ing.find_one({"name": ing_name})
            return ing

    def find_all_user_ing(self):
        user_ing = self.user_ing.find({})
        for ing in user_ing:
            print(ing)

    def delete_user_ing(self, ing_name):
        self.user_ing.delete_one({"name": ing_name})


# client = MongoClient()
# db = client.icc_test
# user_ing = db.user_ing


# add_ing(ing_example, user_ing)
# output_ing = find_ing('apple', user_ing)
# print(output_ing['quantity'])
# print(output_ing)
