import jsonschema
import json
from jsonschema import validate


data = {}
data['ingredient_info'] = []

data['ingredient_info'].append({
    'name': 'green onion',
    'store_method': 'fridge',
    'expiration_duration': 30
})

data['ingredient_info'].append({
    'name': 'onion',
    'store_method': 'room',
    'expiration_duration': 7
})

with open('data.json', 'w') as outfile:
    json.dump(data, outfile)


ing_info_path = './ing_info.json'
ing_info_path = './data.json'
with open(ing_info_path, 'r') as ff:
    ing_info_data = ff.read()
ing_info = json.loads(ing_info_data)
print(ing_info)
