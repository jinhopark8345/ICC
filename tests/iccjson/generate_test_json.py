def make_recipe_info():
    direction = []
    direction.append(["green onion water",500, "g"])
    direction.append(["carrot", 700, "kg"])
    direction.append(["water", 500, "ml"])
    recipes = {}
    recipes['recipe'] = []
    recipes['recipe'].append({
        'name': 'rice cake',
        'like': 7,
        'ings': direction
    })

    recipes['recipe'].append({
        'name': 'curry',
        'like': 5,
        'ings': direction
    })

    return recipes
