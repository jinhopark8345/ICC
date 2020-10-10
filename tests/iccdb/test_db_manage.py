from icc.iccdb.db_manage import *


def make_ing(name, quantity, unit, date):
    return {
        "name": name,
        "quantity": quantity,
        "quantity_unit": unit,
        "store_time": date,
    }


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

    def test_find_user_ing(self):
        # clean up db
        self.icc_db.get_db().drop_collection("user_ing")

        test_apple = make_ing("apple", 400, "g", "2020-10-07 20:34")
        test_onion = make_ing("onion", 400, "g", "2020-10-07 20:34")
        self.icc_db.get_user_ing().insert_one(test_apple)
        self.icc_db.get_user_ing().insert_one(test_onion)

        apple = self.icc_db.find_user_ing("apple")
        assert test_apple == apple

        onion = self.icc_db.find_user_ing("onion")
        assert test_onion == onion

    def test_update_user_ing(self):
        # clean up db
        self.icc_db.get_db().drop_collection("user_ing")

        # add test ings
        db_apple = make_ing("apple", 400, "g", "2020-10-07 20:34")
        db_onion = make_ing("onion", 300, "g", "2020-10-07 20:34")
        self.icc_db.update_user_ing(db_apple)
        self.icc_db.update_user_ing(db_onion)

        test_apple = make_ing("apple", 400, "g", "2020-10-07 20:34")
        test_onion = make_ing("onion", 300, "g", "2020-10-07 20:34")

        # apple = self.icc_db.get_user_ing().find_one({"name": "apple", "_id": False})
        apple = self.icc_db.get_user_ing().find_one({"name":"apple"}, {"_id": False})
        assert test_apple == apple

        onion = self.icc_db.get_user_ing().find_one({"name":"onion"}, {"_id": False})
        assert test_onion == onion

        # apple quantity == 800
        self.icc_db.update_user_ing(db_apple)
        test_apple2 = make_ing("apple", 800, "g", "2020-10-07 20:34")
        find_apple2 = self.icc_db.get_user_ing().find_one({"name":"apple"}, {"_id": False})
        assert test_apple2 == find_apple2

        # apple quantity == 1200
        self.icc_db.update_user_ing(db_apple)
        test_apple3 = make_ing("apple", 1200, "g", "2020-10-07 20:34")
        find_apple3 = self.icc_db.get_user_ing().find_one({"name":"apple"}, {"_id": False})
        assert test_apple3 == find_apple3


    def test_delete_user_ing(self):
        pass
