from iccdb.db_manage import Icc_db
from iccjson.jconnect import make_ing_info, make_user_ing, make_temp_recipe, make_recipe, make_recipe_ing,make_temp_ing_info

from pymongo.results import (InsertOneResult, InsertManyResult, UpdateResult,
                             DeleteResult)


class Test_IccDB:
    @classmethod
    def setup_class(cls):
        "Runs once per class"
        cls.icc_db = IccDB("icc_test")

    @classmethod
    def teardown_class(cls):
        "Runs at end of class"
        # print("teardown calss")
        pass

    def test_add_ing_info(self):
        # clean up db
        self.icc_db.db.drop_collection("ing_info")

        # right case
        db_apple = make_ing_info("apple", "fridge", 3600)
        rtv = self.icc_db.add_ing_info(db_apple)
        assert db_apple == self.icc_db.ing_info.find_one({"name": "apple"})

        # right case #2
        db_onion = make_ing_info("onion", "fridge", 7 * 60 * 24)
        rtv = self.icc_db.add_ing_info(db_onion)
        assert db_onion == self.icc_db.ing_info.find_one({"name": "onion"})

        # return -1 case
        db_watermelon = make_ing_info("wm", "fridge", "7*60*24")
        rtv = self.icc_db.add_ing_info(db_watermelon)
        assert -1 == rtv

        # return -2 case
        rtv = self.icc_db.add_ing_info(db_apple)
        assert -2 == rtv

    def test_update_ing_info(self):
        pass

    def test_delete_ing_info(self):
        # clean up db
        self.icc_db.db.drop_collection("ing_info")

        # delete, non-exist one
        db_apple = make_ing_info("apple", "fridge", 3600)
        assert isinstance(self.icc_db.delete_ing_info("apple"), DeleteResult)

        # delete, exist one
        db_onion = make_ing_info("onion", "fridge", 3600)
        self.icc_db.ing_info.insert_one(db_onion)
        self.icc_db.delete_ing_info("onion")
        assert None == self.icc_db.ing_info.find_one({"name": "onion"})

        # delete, exist one #2
        db_kimchi = make_ing_info("kimchi", "fridge", 3600)
        self.icc_db.ing_info.insert_one(db_kimchi)
        rtv = self.icc_db.delete_ing_info("kimchi")
        assert isinstance(rtv, DeleteResult)
        assert None == self.icc_db.ing_info.find_one({"name": "kimchi"})

    def test_add_user_ing(self):
        # clean up db
        self.icc_db.db.drop_collection("user_ing")

        # add with icc api
        test_apple = make_user_ing("apple", 400, "g", "2020-10-07 20:34")
        test_onion = make_user_ing("onion", 400, "g", "2020-10-07 20:34")
        self.icc_db.add_user_ing(test_apple)
        self.icc_db.add_user_ing(test_onion)

        # test with pymongo api
        db_apple = self.icc_db.user_ing.find_one({"name": "apple"})
        assert test_apple == db_apple

        db_onion = self.icc_db.user_ing.find_one({"name": "onion"})
        assert test_onion == db_onion

    # def test_find_all_user_ing(self):
    #   # clean up db
    #   self.icc_db.db.drop_collection("user_ing")

    #   test_apple = make_user_ing("apple", 400, "g", "2020-10-07 20:34")
    #   test_onion = make_user_ing("onion", 400, "g", "2020-10-07 20:34")
    #   self.icc_db.user_ing.insert_one(test_apple)
    #   self.icc_db.user_ing.insert_one(test_onion)

    #   user_ing = self.icc_db.find_all_user_ing()
    #   print(type(user_ing))

    #   print(user_ing)
    #   for ing in user_ing:
    #     print(ing)

    #   assert False

    def test_update_user_ing(self):
        # clean up db
        self.icc_db.db.drop_collection("user_ing")

        # add test ings
        db_apple = make_user_ing("apple", 400, "g", "2020-10-07 20:34")
        self.icc_db.update_user_ing(db_apple)
        apple = self.icc_db.user_ing.find_one({"name": "apple"})
        assert db_apple == apple

        db_onion = make_user_ing("onion", 300, "g", "2020-10-07 20:34")
        self.icc_db.update_user_ing(db_onion)
        onion = self.icc_db.user_ing.find_one({"name": "onion"})
        assert db_onion == onion

        # apple quantity == 800
        self.icc_db.update_user_ing(db_apple)
        test_apple2 = make_user_ing("apple", 800, "g", "2020-10-07 20:34")
        find_apple2 = self.icc_db.user_ing.find_one({"name": "apple"},
                                                    {"_id": False})
        assert test_apple2 == find_apple2
        # apple quantity == 1200
        self.icc_db.update_user_ing(db_apple)
        test_apple3 = make_user_ing("apple", 1200, "g", "2020-10-07 20:34")
        find_apple3 = self.icc_db.user_ing.find_one({"name": "apple"},
                                                    {"_id": False})
        assert test_apple3 == find_apple3

    def test_delete_user_ing(self):
        # clean up db
        self.icc_db.db.drop_collection("user_ing")

        db_apple = make_user_ing("apple", 400, "g", "2020-10-07 20:34")
        db_onion = make_user_ing("onion", 300, "g", "2020-10-07 20:34")
        self.icc_db.add_user_ing(db_apple)
        self.icc_db.add_user_ing(db_onion)

        assert self.icc_db.find_user_ing("apple") == db_apple
        assert self.icc_db.find_user_ing("onion") == db_onion

        # self.icc_db.print_all_user_ing()

        self.icc_db.delete_user_ing("apple")
        self.icc_db.delete_user_ing("onion")

        assert self.icc_db.find_user_ing("apple") == None
        assert self.icc_db.find_user_ing("onion") == None

    def test_add_recipe(self):
        # clean up db
        self.icc_db.db.drop_collection("recipe")

        recipes = make_temp_recipe()
        rec0 = recipes[0]
        rec1 = recipes[1]

        rtv0 = self.icc_db.add_recipe(rec0)
        rtv1 = self.icc_db.add_recipe(rec1)
        # print("rtv0: ", rtv0)
        # print("rtv1: ", rtv1)

        rice_cake = self.icc_db.recipe.find_one({"name": "rice cake soup"})
        curry = self.icc_db.recipe.find_one({"name": "curry"})
        assert rec0 == rice_cake
        assert rec1 == curry

    def test_delete_recipe(self):
        # clean up db
        self.icc_db.db.drop_collection("recipe")

        recipes = make_temp_recipe()
        rec0 = recipes[0]
        rec1 = recipes[1]

        rtv0 = self.icc_db.add_recipe(rec0)
        rtv1 = self.icc_db.add_recipe(rec1)

        self.icc_db.delete_recipe("rice cake")
        self.icc_db.delete_recipe("curry")

        # assert rec0 == rice_cake
        # assert rec1 == curry

        assert self.icc_db.find_recipe("rice cake") == None
        assert self.icc_db.find_recipe("curry") == None

    def test_replace_recipe_like(self):
        # clean up db
        self.icc_db.db.drop_collection("recipe")
        recipes = make_temp_recipe()
        rec0 = recipes[0]
        rtv0 = self.icc_db.add_recipe(rec0)

        # case1 : like test
        rec0["like"] += 7
        # print("rec0: ", rec0)
        self.icc_db.replace_recipe_like(rec0)
        # print("rec0: ", rec0)
        # print("rec0 db: ", self.icc_db.find_recipe(rec0["name"]))
        # print("rec0 db: ", self.icc_db.find_recipe(rec0["name"], False))
        assert self.icc_db.find_recipe(rec0["name"]) == rec0

        # error
    def test_replace_recipe_ings(self):
        # clean up db
        self.icc_db.db.drop_collection("recipe")
        recipes = make_temp_recipe()
        rec0 = recipes[0]
        rtv0 = self.icc_db.add_recipe(rec0)

        # case2: ing
        # rec0["like"] += 7
        rec0["ings"][0]['quantity'] += 500
        self.icc_db.replace_recipe_ings(rec0)

        # print("rec0: ", rec0)
        # print("rec0 db: ", self.icc_db.find_recipe(rec0["name"]))
        assert self.icc_db.find_recipe(rec0["name"]) == rec0

    def test_update_recipe_like(self):
        # clean up db
        self.icc_db.db.drop_collection("recipe")
        recipes = make_temp_recipe()
        rec0 = recipes[0]
        rtv0 = self.icc_db.add_recipe(rec0)

        # add like 1
        rec0["like"] += 1
        self.icc_db.update_recipe_like(rec0["name"])

        # assert self.icc_db.find_recipe(rec0["name"]) == rec0
        print("rec0: ", rec0)
        print("db rec0", self.icc_db.find_recipe(rec0["name"]))

        # add like 4
        rec0["like"] += 4
        self.icc_db.update_recipe_like(rec0["name"], 4)
        assert self.icc_db.find_recipe(rec0["name"]) == rec0

        # replace like
        rec0["like"] = 20
        self.icc_db.update_recipe_like(rec0["name"], 20, True)
        assert self.icc_db.find_recipe(rec0["name"]) == rec0

    def test_add_recipe_ing(self):
        # clean up db
        self.icc_db.db.drop_collection("recipe")
        recipes = make_temp_recipe()
        rec0 = recipes[0]
        rtv0 = self.icc_db.add_recipe(rec0)

        # print(rec0)

        db_watermelon = make_recipe_ing("wm", 700, 'g')
        db_onion = make_recipe_ing("onion", 7 * 60 * 24, "g")
        db_apple = make_recipe_ing("apple", 3600, "kg")

        self.icc_db.add_recipe_ing(rec0["name"], db_apple)

        assert self.icc_db.find_recipe_ing(rec0["name"], "apple") == db_apple

    def test_delete_recipe_ing(self):
        # clean up db
        self.icc_db.db.drop_collection("recipe")
        recipes = make_temp_recipe()
        rec0 = recipes[0]
        rtv0 = self.icc_db.add_recipe(rec0)

        db_watermelon = make_recipe_ing("wm", 700, 'g')
        db_onion = make_recipe_ing("onion", 7 * 60 * 24, "g")
        db_apple = make_recipe_ing("apple", 3600, "kg")

        self.icc_db.add_recipe_ing(rec0["name"], db_apple)
        self.icc_db.delete_recipe_ing(rec0["name"], "apple")

        assert self.icc_db.find_recipe_ing(rec0["name"], "onion") == None

    def test_update_recipe_ing(self):
        # clean up db
        self.icc_db.db.drop_collection("recipe")
        recipes = make_temp_recipe()
        rec0 = recipes[0]
        rtv0 = self.icc_db.add_recipe(rec0)

        db_watermelon = make_recipe_ing("wm", 700, 'g')
        db_onion = make_recipe_ing("onion", 7 * 60 * 24, "g")
        db_apple = make_recipe_ing("apple", 3600, "kg")

        self.icc_db.add_recipe_ing(rec0["name"], db_onion)

        # case1: replace
        db_onion2 = make_recipe_ing("onion", 5000, "g")
        self.icc_db.update_recipe_ing(rec0["name"],
                                      db_onion2,
                                      replace_flag=True)
        # print(self.icc_db.find_recipe_ing(rec0["name"], "onion"))
        # print(db_onion2)
        assert self.icc_db.find_recipe_ing(rec0["name"], "onion") == db_onion2

        # case2: update
        db_onion3 = make_recipe_ing("onion", 3, "g")
        db_onion2["quantity"] += db_onion3["quantity"]

        self.icc_db.update_recipe_ing(rec0["name"],
                                      db_onion3,
                                      replace_flag=False)
        # print(self.icc_db.find_recipe_ing(rec0["name"], "onion"))
        # print(db_onion2)

        assert self.icc_db.find_recipe_ing(rec0["name"], "onion") == db_onion2

    def test_find_ing_info(self):
        # clean up db
        self.icc_db.db.drop_collection("ing_info")

        # find, exist one
        db_apple = make_ing_info("apple", "fridge", 3600)
        self.icc_db.ing_info.insert_one(db_apple)
        rtv = self.icc_db.find_ing_info("apple")
        assert db_apple == rtv

        # find, non-exist one
        rtv = self.icc_db.find_ing_info("onion")
        assert rtv == None

    def test_find_user_ing(self):
        # clean up db
        self.icc_db.db.drop_collection("user_ing")

        test_apple = make_user_ing("apple", 400, "g", "2020-10-07 20:34")
        test_onion = make_user_ing("onion", 400, "g", "2020-10-07 20:34")
        self.icc_db.user_ing.insert_one(test_apple)
        self.icc_db.user_ing.insert_one(test_onion)

        apple = self.icc_db.find_user_ing("apple")
        assert test_apple == apple

        onion = self.icc_db.find_user_ing("onion")
        assert test_onion == onion

    def test_find_recipe(self):
        # clean up db
        self.icc_db.db.drop_collection("recipe")
        recipes = make_temp_recipe()
        rec0 = recipes[0]
        rtv0 = self.icc_db.add_recipe(rec0)

        assert self.icc_db.find_recipe(rec0["name"]) == rec0

    def test_find_recipes(self):
        # clean up db
        self.icc_db.db.drop_collection("recipe")
        recipes = make_temp_recipe()

        for recipe in recipes:
            rtv = self.icc_db.add_recipe(recipe)
            print(rtv)

        # print(recipes)
        # print(self.icc_db.find_recipes())

        assert self.icc_db.find_recipes() == recipes

    def test_find_recipe_ing(self):
        # clean up db
        self.icc_db.db.drop_collection("recipe")
        recipes = make_temp_recipe()
        rec0 = recipes[0]
        rtv0 = self.icc_db.add_recipe(rec0)

        # db_watermelon = make_recipe_ing("wm", 700, 'g')
        # db_onion = make_recipe_ing("onion", 7 * 60 * 24, "g")
        # db_apple = make_recipe_ing("apple", 3600, "kg")

        # self.icc_db.add_recipe_ing(rec0["name"], db_apple)

        # assert self.icc_db.find_recipe_ing(rec0["name"], "apple") == db_apple

        recipe_name = rec0["name"]

        ing = make_recipe_ing("jinho", 500, 'g')
        ing2 = make_recipe_ing("jaehyun", 700, 'g')

        rtv = self.icc_db.add_recipe_ing(recipe_name, ing)
        rtv2 = self.icc_db.add_recipe_ing(recipe_name, ing2)

        assert self.icc_db.find_recipe_ing(recipe_name, "jinho") == ing
        assert self.icc_db.find_recipe_ing(recipe_name, "jaehyun") == ing2

    def test_find_user_ings(self):
        # clean up db
        self.icc_db.db.drop_collection("user_ing")

        # add with icc user ing
        test = []
        test_apple = make_user_ing("apple", 400, "g", "2020-10-07 20:34")
        test_onion = make_user_ing("onion", 400, "g", "2020-10-07 20:34")
        test.append(test_apple)
        test.append(test_onion)

        self.icc_db.add_user_ing(test_apple)
        self.icc_db.add_user_ing(test_onion)

        assert self.icc_db.find_user_ings() == test

    def test_find_ing_infos(self):
        ### find_ing_infos(returnID=True ) 인 이유는?

        # clean up db
        self.icc_db.db.drop_collection("ing_info")

        # right case
        db_apple = make_ing_info("apple", "fridge", 3600)
        db_onion = make_ing_info("onion", "fridge", 7 * 60 * 24)
        self.icc_db.add_ing_info(db_apple)
        self.icc_db.add_ing_info(db_onion)

        test = []
        test.append(db_apple)
        test.append(db_onion)

        print(test)
        print(self.icc_db.find_ing_infos())
        assert self.icc_db.find_ing_infos(True) == test

    def test_add_temp_recipe(self):
        self.icc_db.add_temp_recipe()
        recipe = make_temp_recipe()

        assert self.icc_db.find_recipes(False) == recipe

    def test_add_temp_ing_info(self):
        # clean up db
        self.icc_db.db.drop_collection("ing_info")

        ##### error -> 겹치는 것 있을 때 문제점 해결가능.
        self.icc_db.add_temp_ing_info()
        ing_infos = make_temp_ing_info()
        print(len(ing_infos))
        print(len(self.icc_db.find_ing_infos(False)))
        assert self.icc_db.find_ing_infos(False) == ing_infos
