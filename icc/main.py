from iccjson.jconnect import *
from recommend.compare_recipe import *
from recommend.recommend_recipe import *
from iccdb.db_manage import *


user_ings = get_data("user_ing")
recipes = get_data("recipe")

recipes_needed_ings = []

def main():
  # print("user_ings: {}".format(user_ings))
  for recipe in recipes:

    print("making: {}...".format(recipe["name"]))
    need_ings = get_need_ings(recipe, user_ings)
    print("need: {}...".format(need_ings))

    print("cur_need quantity", get_total_quantity(need_ings))
    cur_total_quan = get_total_quantity(need_ings)

    # collect need ings quantity
    recipes_needed_ings.append(([cur_total_quan, recipe["name"]]))

  # recommend one recipe based on needed quantity
  rec_recipe = recommend_recipe(recipes_needed_ings)
  print(rec_recipe)

# main()

icc_db = Icc_db("icc")

# def make_ing(name, quantity, unit, date):
#   return {
#       "name": name,
#       "quantity": quantity,
#       "quantity_unit": unit,
#       "store_time": date,
#   }

def main_t():
  # icc_db.get_db().drop_collection("user_ing")
  print("before")
  icc_db.find_all_user_ing()

  # ing_example = make_ing("onion2", 500)
  ing_example = make_user_ing("apple", 400, "g", "2020-10-07 20:34")
  # icc_db.add_user_ing(ing_example)

  # icc_db.delete_user_ing("apple")

  # temp_ing = icc_db.find_user_ing("apple", False)
  # print(temp_ing)

  temp = icc_db.update_user_ing(ing_example)
  print(temp)
  # onion_ing = icc_db.find_user_ing("onion")
  # temp = icc_db.find_all_user_ing()

  # print out all user_ing
  print("after")
  icc_db.find_all_user_ing()

  # print(temp)
  # print(onion_ing)

main_t()


# from app import app
# if __name__ == '__main__':
#     app.run()
