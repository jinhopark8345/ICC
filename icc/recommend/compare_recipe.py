"""
compare recpie API
"""


def is_comparable(ask_ing, user_ing):
  """tell if the ingredients are comparable

    Args:
        ask_ing: ingredient from recipe
        user_ing: ingredient from user

    Returns:
        return True if they have same name and same quantity_unit

    """

  if (ask_ing["name"] == user_ing["name"]) and (ask_ing["quantity_unit"]
                                                == user_ing["quantity_unit"]):
    return True

  return False


def get_diff_ing(ask_ing, user_ing):
  """compare two "same" ingredients

    Args:
        ask_ing: ingredient from recipe
        user_ing: ingredient from user

    Returns:
        return the dictionary of difference in terms of quantity

    """
  if is_comparable(ask_ing, user_ing):
    diff_quantity = ask_ing["quantity"] - user_ing["quantity"]
    user_ing["quantity"] = diff_quantity
    return user_ing
  else:
    print("wrong use case")


def get_need_ing(ask_ing, user_ings):
  """how much more "ask_ingredient" does user need?
    compare "ask_ingredient" that user need from user_ingredients"

        Args:
           ask_ing: A ingredient from a recipe
           user_ings: ingredinets that user has

        Returns:
            if user has the ingredient with same name, then return the
            quantity that user need if user does not have the
            ingredient with same name, then return the whole
            ingredient the recipe require

    """

  need_ing = next(
      ((get_diff_ing(ask_ing, user_ing))
       for user_ing in user_ings if is_comparable(ask_ing, user_ing)), ask_ing)

  return need_ing


def get_need_ings(recipe, user_ings):
  """find ingredinets that user need to make the recipe

    Args:
       user_ings [] ingreidents that user has
       recipe recipe that user tries to make

    Returns:
        ingredients that user need to make the recipe

    """
  need_user_ings = [
      get_need_ing(cur_need_ing, user_ings) for cur_need_ing in recipe["ings"]
  ]

  need_user_ings = [ing for ing in need_user_ings if ing["quantity"] > 0]
  return need_user_ings


