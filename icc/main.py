
from iccjson.schema import *

recipe_schema = get_schema("recipe")
recipe_test = get_test("recipe")
recipe_data = get_data("recipe")

print(recipe_schema)
print(recipe_test)
print(recipe_data)
