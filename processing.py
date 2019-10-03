import pandas as pd


def parsify(parent="Food.csv"):
    thing = pd.read_csv(parent).values
    # print(thing[:, 1])
    # print(thing[:, 7])
    food = thing[:, 0]
    ing = thing[:, 1]
    delete = [
        [" (FOR COLOR)", ""],
        ["ONE OR MORE OF THE FOLLOWING: ", ""],
        [" (", ", "],
        [")", ""],
        ["INGREDIENTS: ", ""],
        [".", ""],
        [" CONTAINS 2% OR LESS OF: ", ", "],
        [" CONTAINS 1% OR LESS OF: ", ", "]
    ]
    for ii in range(len(ing)):
        canPlay = True
        for word in delete:
            try:
                ing[ii] = word[1].join(ing[ii].split(word[0]))
            except:
                ing[ii] = float("NaN")
                canPlay = False
        if canPlay:
            ing[ii] = ing[ii].split(", ")
    return [food, ing]
