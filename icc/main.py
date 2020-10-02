from iccjson.schema import *
from iccjson.function import *

#from tests.iccjson.iccjson_test import *

#recipe_schema = get_schema("recipe")
#recipe_test = get_test("recipe")
#recipe_data = get_data("recipe")

#ingredient_info_schema = get_schema("ing_info")
#ingredient_info_test = get_test("ing_info")

user_ing = get_data("user_ing")

#print(recipe_schema)
#print(recipe_test)
#print(recipe_data)

#print(ingredient_info_schema)
#print(ingredient_info_test)

#print(user_ing)

#find_recipe_ing()
user_ing_data = get_data("user_ing")
recipe_data = get_data("recipe")
compare_data = compare_ing(user_ing_data,recipe_data)
print(compare_data)

need_data = need_recipe(recipe_data, compare_data)
recommend_recipe = recommend_recipe(need_data,recipe_data)


print(recommend_recipe)

