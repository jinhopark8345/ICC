from iccdb.db_manage import Icc_db
from iccjson.jconnect import make_ing_info, make_user_ing

from pymongo.results import (InsertOneResult, InsertManyResult, UpdateResult,
                             DeleteResult)


class Test_Icc_db:
  @classmethod
  def setup_class(cls):
    "Runs once per class"
    cls.icc_db = Icc_db("icc_test")

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



  def test_test(self):
    pass
    # ing = self.icc_db.user_ing.find_one({"name": "onion"})
    # print(ing)

    # ing = self.icc_db.user_ing.find_one({"name": "onion"}, {"_id": False})
    # print(ing)
    # assert False
