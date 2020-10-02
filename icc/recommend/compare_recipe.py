def get_diff_ing(ask_ing, user_ing):
    """ compare two ingredient if they have same name return the difference in terms of quantity"""
    ing = {}

    if ing["name"] == ask_ing["name"]:
        ing["quantity"] = ask_ing["quantity"] - user_ing["quantity"]
        ing["quantity_unit"] = ask_ing["quantity_unit"]

    return ing


# how much more "ask_ingredient" does user need?
# compare "ask_ingredient" that user need from "user_ingredients"
# ask_ing : ingredient that user need to make the recipe
# user_ings : ingredients user has
def get_need_ing(ask_ing, user_ings):
    # new_dict = dict((item['id'], item) for item in initial_list)
    # match_ing = dict((user_ing) for user_ing in user_ings if user_ing['name'] == ask_ing['name'])
    match_ing = next(
        (user_ing for user_ing in user_ings if user_ing["name"] == ask_ing["name"]),
        None,
    )

    if match_ing != None:
        return get_diff_ing(ask_ing, match_ing)

    else:
        return ask_ing


# find ingredient"s" that user need to make the one recipe
# user_ings : ingredients user has
# recipe: recipe that user tries to make
def get_need_ings(user_ings, recipe):
    need_recipe_ings = []
    for cur_recipe_ing in recipe["ings"]:
        cur_need_ing = get_need_ing(cur_recipe_ing, user_ings)
        need_recipe_ings.append(cur_need_ing)

    return need_recipe_ings
