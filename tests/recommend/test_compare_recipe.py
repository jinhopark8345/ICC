from iccjson.jconnect import *
from recommend.compare_recipe import *


def make_ing(name, quantity, unit):
    return {"name": name, "quantity": quantity, "quantity_unit": unit}


def make_ings_user(ings_len):

    ing3 = make_ing("onion", 500, "g")
    ing4 = make_ing("red onion", 400, "g")
    ing5 = make_ing("kimchi", 300, "g")
    # for i in range(ings_len):

    return [ing3, ing4, ing5]


def make_ings_recipe(ings_len):

    ing3 = make_ing("onion", 500, "g")
    ing5 = make_ing("kimchi", 300, "g")
    # for i in range(ings_len):

    return [ing3, ing5]


def test_is_comparable():

    # same name, same quantity unit
    ing1 = make_ing("onion", 500, "g")
    ing2 = make_ing("onion", 400, "g")
    is_comp = is_comparable(ing1, ing2)
    assert is_comp == True

    # diff name ings
    ing3 = make_ing("onion", 500, "g")
    ing4 = make_ing("red onion", 400, "g")
    is_comp2 = is_comparable(ing3, ing4)
    assert is_comp2 == False

    # diff quan_unit ings
    ing5 = make_ing("onion", 500, "g")
    ing6 = make_ing("onion", 400, "kg")
    is_comp3 = is_comparable(ing5, ing6)
    assert is_comp3 == False


def test_get_diff_ing():
    ing1 = make_ing("onion", 500, "g")
    ing2 = make_ing("onion", 400, "g")
    diff = get_diff_ing(ing1, ing2)
    assert diff["quantity"] == 100

    ing3 = make_ing("red onion", 300, "g")
    ing4 = make_ing("red onion", 600, "g")
    diff2 = get_diff_ing(ing3, ing4)
    assert diff2["quantity"] == -300


def test_get_need_ing():

    # recipe = make_ings_recipe()
    ing1 = make_ing("onion", 500, "g")

    ing3 = make_ing("onion", 100, "g")
    ing4 = make_ing("red onion", 400, "g")
    ing5 = make_ing("apple", 400, "g")
    user_ings = [ing3, ing4, ing5]

    result_ing = make_ing("onion", ing1["quantity"] - ing3["quantity"], "g")
    assert get_need_ing(ing1, user_ings) == result_ing

    ing2 = make_ing("tree", 10, "g")
    result_ing2 = ing2
    assert get_need_ing(ing2, user_ings) == result_ing2


def test_get_need_ings():

    ing1 = make_ing("onion", 500, "g")
    ing2 = make_ing("tree", 10, "g")
    recipe_ings = [ing1, ing2]
    recipe = {"ings": recipe_ings}

    ing3 = make_ing("onion", 100, "g")
    ing4 = make_ing("red onion", 400, "g")
    ing5 = make_ing("apple", 400, "g")
    user_ings = [ing3, ing4, ing5]

    answer_ing = make_ing("onion", ing1["quantity"] - ing3["quantity"], "g")
    answer_ing2 = ing2
    answer_ings = [answer_ing, answer_ing2]

    result_ings = get_need_ings(recipe, user_ings)

    assert result_ings == answer_ings
