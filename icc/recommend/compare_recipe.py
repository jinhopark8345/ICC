
# compare two ingredient and return difference
def get_diff_ing(ask_ing, user_ing):
    ing = []

    # append ing name
    ing.append(ask_ing[0])
    # append quantity diff
    ing.append(ask_ing[1] - user_ing['quantity'])
    # append unit
    ing.append(ask_ing[2])

    return ing

# how much more "the ingredient" does user need?
def need_ing(ask_ing, user_ing_data):
    for cur_user_ing in user_ing_data:
        # 찾는 재료가, 유저한테 있을 경우 -> 필요한 양 리턴
        if ask_ing[0] in cur_user_ing['name']:
            return get_diff_ing(ask_ing, cur_user_ing)
        # 찾는 재료가, 유저한테 없을 경우 ->
        else:
            return ask_ing


# find need ingredient"s" from "one" recipe
def need_recipe(user_ing_data, recipe):

    need_ings = []
    for j in range(len(recipe['ings'])):
        cur_recipe_ing = recipe['ings'][j]
        cur_need_ing = need_ing(cur_recipe_ing, user_ing_data)
        need_ings.append(cur_need_ing)
    return need_ings;

