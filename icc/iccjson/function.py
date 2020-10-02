import copy
from iccjson.schema import *




def print_test():
    cur_dir = os.path.dirname(os.path.realpath(__file__))
    print("function_Test")



def compare_ing(user_ing_data,recipe_data): ####### compare user_ing and recipe_ing 냉장고에 있는 재료와 레시피에 있는 재료 비
    
    compare_data =copy.deepcopy( recipe_data )
   
    
    for i in range ( len(recipe_data) ):
        for j in range( len(recipe_data[i]['ings']) ):      
            for k in range( len(user_ing_data) ):
                if recipe_data[i]['ings'][j][0] == user_ing_data[k]['name']:
                    recipe_data[i]['ings'][j][1] = user_ing_data[k]['quantity']
                    break
                else:
                    recipe_data[i]['ings'][j][1] = 0       
                              
    return compare_data;

def need_recipe(recipe_data, compare_data):
    need_data = copy.deepcopy( recipe_data )
    print(recipe_data[0]['ings'][0][1])
    for i in range ( len(recipe_data) ):
        for j in range( len(recipe_data[i]['ings']) ):
            need_data[i]['ings'][j][1]=recipe_data[i]['ings'][j][1] - compare_data[i]['ings'][j][1] 
    

    return need_data

def recommend_recipe(need_data):
    recom
    for i in range ( len(need_data) ):
        for j in range( len(need_data[i]['ings']) ):
             need_data[
           




    return recommed_recipe






    
    
