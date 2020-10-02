def get_total_quantity(need_ings):
    """get sum of quantity of ingredients that user needs to make the recipe

    Args:
       need_ings ingredients that user needs

    Returns:
        sum of quantity

    """
    return sum([ing["quantity"] for ing in need_ings])


def recommend_recipe(recipes_need_quantity):
    """find smallest quantity among quantities

    Args:
        recipes_need_quantity list of quantity total, each quantity total
       show how much quantity user needs to make the recipe

    Returns:
        name of the recipe

    """

    ing = min(recipes_need_quantity, key=lambda recipe: recipe[0])
    return ing[1]
