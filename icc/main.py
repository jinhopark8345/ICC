from iccjson.schema import *
from 


recipe_schema = get_schema("recipe")
recipe_test = get_test("recipe")
recipe_data = get_data("recipe")

ingredient_info_schema = get_schema("ing_info")
ingredient_info_test = get_test("ing_info")
ingredient_info_data = get_data("ing_info")

#print(recipe_schema)
print(recipe_test)
#print(recipe_data)

#print(ingredient_info_schema)
print(ingredient_info_test)
#print(ingredient_info_data)
