
# compare two ingredient and return difference
def get_diff_ing(ask_ing, user_ing):
    ing = []

    # append ing name
    ing.append(ask_ing['name'])
    # append quantity diff
    # print(ask_ing['quantity'])
    # print(user_ing['quantity'])
    ing.append(ask_ing['quantity'] - user_ing['quantity'])
    # append unit
    ing.append(ask_ing['quantity_unit'])

    return ing

# how much more "the ingredient" does user need?
def get_need_ing(ask_ing, user_ings):
    print("user_ings: {}, user_ings_len: {}".format(user_ings, len(user_ings)))
    for ing in user_ings:
        print("need_ing function, each ing:",ing)

        # 찾는 재료가, 유저한테 있을 경우 -> 필요한 양 리턴
        if ask_ing['name'] in ing['name']:
            return get_diff_ing(ask_ing, ing)

        # 찾는 재료가, 유저한테 없을 경우
        else:
            return ask_ing


# find need ingredient"s" from "one" recipe
def need_recipe(user_ings, recipe):
    # print(recipe)

    need_ings = []
    # for j in range(len(recipe['ings'])):
    #     cur_recipe_ing = recipe['ings'][j]
    #     cur_need_ing = need_ing(cur_recipe_ing, user_ings)
    #     need_ings.append(cur_need_ing)
    # return need_ings;

    # print("need_recipe, recipe: ", recipe['ings'])
    # print("need_recipe, recipe[1]: ", recipe['ings'][1])

    for cur_recipe_ing in recipe['ings']:
        print(cur_recipe_ing['name'])
        cur_need_ing = get_need_ing(cur_recipe_ing, user_ings)
        need_ings.append(cur_need_ing)

    return need_ings
