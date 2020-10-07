from iccjson.jconnect import *
from recommend.compare_recipe import *
from recommend.recommend_recipe import *
from iccdb.db_manage import *

# from tests.iccjson.test_jconnect import *
# from iccjson.test_jconnect import *

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

icc_db = Icc_db('icc')

def make_ing(name, quantity, unit, date):
    return {
        "name": name,
        "quantity": quantity,
        "quantity_unit": unit,
        "store_time": date,
    }

ing_example = make_ing("onion", 500, "g", "2020-10-07 13:34")
# ing_example = make_ing("apple", 400, "g", "2020-10-07 20:34")

# icc_db.add_user_ing(ing_example)
onion_ing = icc_db.find_user_ing('onion')
print(onion_ing)
