from iccjson.jconnect import *
from recommend.compare_recipe import *
from recommend.recommend_recipe import *

user_ings = get_data("user_ing")
recipes = get_data("recipe")


recipes_needed_ings = []

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
