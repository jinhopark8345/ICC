# need 에 값에 따라 가중치 부여
def get_total_quantity(need_ings):

    total_quan = 0
    for ing in need_ings:
        total_quan = total_quan + ing[1]

    return total_quan

# def jin_temp(recipe):
#     return recipe[0]
def recommend_recipe(recipes_need_quantity):
    ing = min(recipes_need_quantity, key= lambda recipe:recipe[0])
    # ing = min(recipes_need_quantity, key= jin_temp)
    return ing[1]
