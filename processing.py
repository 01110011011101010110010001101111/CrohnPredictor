import pandas as pd


def parsify(parent="Food.csv"):
    thing = pd.read_csv(parent).values
    food = thing[:, 0]
    ing = thing[:, 1]
    delete = [
        [" (FOR COLOR)", ""],
        ["ONE OR MORE OF THE FOLLOWING: ", ""],
        ["MAY CONTAIN ", ""],
        [" (", ", "],
        [")", ""],
        ["INGREDIENTS: ", ""],
        [".", ""],
        [" CONTAINS 2% OR LESS OF: ", ", "],
        [" CONTAINS 1% OR LESS OF: ", ", "],
        [" AND/OR ", ", "],
        ["CONTAINS: ", ""],
        ["CONTAINS ", ""],
        [";", ","],
        ["],", ","],
        [" [", ", "],
        ["CONTAINS, ", ""],
        ["CONTAINS:", ""],
        ["2% OR LESS OF ", ""],
        [": ", ", "],
        [" CONTAINS2% OR LESS OF,", ""],
        ["CONTAINS2% OR LESS OF", ""],
        [" ALSO CONTAINS- ", ", "],
        [" ALSO CONTAINS-", ", "],
        ["LESS THAN 2% OF, ", ""],
        ["LESS THAN 2% OF ", ""],
        ["LESS THAN 1% OF ", ""],
        ["LESS THAN 1% OF, ", ""],
        ["LESS THAN 2% ", ""],
        ["LESS THAN 2%, ", ""],
        [" {", ", "],
        ["{", ", "],
        ["}", ""],
        [", SALT", ""],
        [", WITH SALT", ""], 
        [", SEA SALT", ""],
        [", WITH SALT ADDED", ""], 
        [", AND SALT", ""],
        [", FILTERED WATER", ""],
        [", WATER", ""]
    ]
    semiabsurd = [ 
        "WATER",
        "SALT"
    ]
    for ii in range(len(ing)):
        if type(ing[ii]) == str: ing[ii] = ing[ii].upper()
        canPlay = True
        for word in delete:
            try:
                ing[ii] = word[1].join(ing[ii].split(word[0]))
            except:
                ing[ii] = float("NaN")
                canPlay = False
        if canPlay:
            ing[ii] = ing[ii].split(", ")
            for i in semiabsurd:
                try: 
                    ing[ii].remove(i)
                    # print("NO SALT")
                except:
                    pass

    return [food, ing]
