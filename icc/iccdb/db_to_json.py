def add_ing_temp():

    ing3 = make_ing("watermelon sugar", 500, "g", "2020-10-07 13:34")
    ing4 = make_ing("watermelon sugar3", 500, "g", "2020-10-07 13:34")
    ing5 = make_ing("watermelon sugar2", 500, "g", "2020-10-07 13:34")
    ings = [ing3, ing4, ing5]

    cur_dir = os.path.dirname(os.path.realpath(__file__))
    user_ing_path = cur_dir + "/user_ing.json"
    print(user_ing_path)

    with open(user_ing_path, "w") as outfile:
        # json.dump(ing3, outfile)
        # json.dump(ing3, outfile)
        outfile.write(json.dumps(ings))


# add_ing_temp()
