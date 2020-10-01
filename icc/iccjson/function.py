
from iccjson.schema import *




def print_test():
    cur_dir = os.path.dirname(os.path.realpath(__file__))
    print("function_Test")


def find_recipe_ing(): ## 레시피에서 사용하느 재료 찾기.
    cur_dir = os.path.dirname(os.path.realpath(__file__))
    temp_data = get_data("recipe")
    recipe_name_data = []
    recipe_ing_data = []
    #print("temp_data : ",temp_data[1]['ings'])
    for i in range ( len(temp_data) ):
        recipe_ing_data.append( temp_data[i]['ings'] )
        recipe_name_data.append( temp_data[i]['name'] )



    print(recipe_ing_data[0])
    print(recipe_name_data[0])
    
    
   


def search_recipe():
    return 0
