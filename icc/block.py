# 이름 고정
user_ingredient = {
    "name": "green onion",
    "quantity": "500",
    "quantity_unit": "g",
    "store_time": "2020-09-27 11:43",
}

# 이름 바꿔야함
ingredient_info = {
    "name": "green onion",
    "store method": "fridge",
    "expiration duration": "3600 * 24 * 7",
    "image": "something",
}

recipe = {
    "name": "떡국",
    "호감도": 5,
    "ingredient": {
        ["양파", "500g"],
        ["대파", "200g"],
        ["계란", "200g"],
    },
    "portion": 2,
    "direction": {
        ["물을 끓이세요", "image-file.com"],
        ["재료를 준비하세요", "image-file.com"],
    },
}

recipe = {
    "name": "떡국",
    "호감도": 5,
    "ingredient": {
        [
            "양파",
            "500g"
        ],
        [
            "대파",
            "200g"
        ],
        [
            "계란",
            "200g"
        ],
    },
    "portion": 2,
    "direction": {
        [
            "물을 끓이세요",
            "image-file.com"
        ],
        [
            "재료를 준비하세요",
            "image-file.com"
        ],
    },
}
