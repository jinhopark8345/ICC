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

# print(ing_info)

ing_info_temp = ing_info['ingredient_info'][1]
print(ing_info_temp) # {'name': 'onion', 'store_method': 'room', 'expiration_duration': 7}

# test if ing_info_temp is valid
def validateJson(jsonData, schema):
    try:
        validate(instance=jsonData, schema=schema)
    except jsonschema.exceptions.ValidationError as err:
        return False
    return True

ing_info_schema_path = '../json/ing_info_schema.json'
with open(ing_info_schema_path, 'r') as f:
    ing_info_schema_data = f.read()
ing_info_schema = json.loads(ing_info_schema_data)

isValid = validateJson(ing_info_temp, ing_info_schema)
print(isValid)
