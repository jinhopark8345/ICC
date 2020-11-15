from iccjson.jconnect import *
from recommend.compare_recipe import *
from recommend.recommend_recipe import *
from iccdb.db_manage import *


def main_t():

    icc_db = Icc_db("icc")
    icc_db.add_temp_recipe()
    icc_db.add_temp_user_ing()
    icc_db.add_temp_ing_info()

    recommended_recipe = recommed_recipe()
    print("you should make {}".format(recommended_recipe))

    print("before user ings {}".format(icc_db.find_user_ings(returnID=False)))
    remove_recipe_ing_from_user_ing(recommended_recipe)
    print("after user ings {}".format(icc_db.find_user_ings(returnID=False)))
    remove_recipe_ing_from_user_ing(recommended_recipe)
    print("after user ings {}".format(icc_db.find_user_ings(returnID=False)))

main_t()
