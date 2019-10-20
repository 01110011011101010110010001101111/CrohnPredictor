import pandas as pd
import numpy as np


def parsify(parent="Food.csv"):
    thing = pd.read_csv(parent).values
    INGREDIENT_LIMIT = 200
    food = thing[:, 0]
    ing = thing[:, 1]
    findFood = ["BARBECUE SAUCE", "MUSTARD", "PIZZA CRUST",
                "SORBET", "HUMMUS", "GELATO", "SPAGHETTI", "MACARONI", "PASTA SAUCE", 
                "TOMATO SAUCE", "CHEDDAR CHEESE", "CORN TORTILLA CHIPS", "SOUR PATCH", 
                "FRESH GROUND BEEF", "BLENDED LOW-FAT GREEK YOGURT", "ORGANIC PROTEIN POWDER",
                "ORANGE JUICE", "CORNBREAD CRISPS", "ORGANIC TORTILLA CHIPS", "STRING CHEESE", 
                "SPARKLING ITALIAN SODA", "MAPLE PORK SAUSAGE", "BURGER", "BEEF PATTIES", "PIZZA SAUCE",
                "WALNUT BUTTER", "COCONUT OIL", "SHREDDED 4 CHEESE MEXICAN BLEND", "COTTAGE CHEESE",
                "GRANOLA BARS", "MOCHI", "MOZZARELLA CHEESE", "PIZZA", "BAKING FLOUR", "RITZ CRACKERS",
                "UNCURED HAM", "HIGH PROTEIN BARS", "FILLED MILK CHOCOLATE BAR", "PROTEIN CAKES", "AUTHENTIC CITRUS SODA",
                "SUPER PREMIUM ICE CREAM", "BAGELS", "SPARKLING WATER", "PROTEIN & FIBER BARS", "SOUR CREAM", "GRANOLA BAR",
                "DILL PICKLE", "PROPEL", "HARD CANDY", "GREEK NONFAT YOGURT", "WHEAT CEREAL", "KETCHUP", "MAYONNAISE", "POCKET SANDWICH",
                "VINEGAR", "PURE NON-CARBONATED WATER", "Chex Mix", "LEMONADE", "Coca-Cola", "Diet Coke", "ALOE VERA DRINK", "TROPICS ICE CREAM",
                "JELLY MINI STICK"]
    companies = ["FRESH & EASY", "NABISCO",
                 "McCafe", "STATER BROS.", "GREAT MIDWEST", "MARANATHA", "NANCY'S", 
                 "PRAEGER'S", "ANDREW & EVERETT", "MARIANO'S", "ROUNDY'S", "HOLA", "AMAZONAS", 
                 "PACIFIC SURF", "ALBERTSON'S", "ESSENTIAL EVERYDAY", "CLANCY'S", "MADHAVA", "SCHNUCKS",
                 "JOHN WM. MACY'S", "FOLLOW YOUR HEART", "STAHLBUSH ISLAND FARMS", "Totino's", "PINES",
                 "CADBURY", "TOBLERONE", "GREEN & BLACK'S", "NATURE'S GARDEN", "FAIRWAY", 
                 "ELLA'S", "SARAH", "NICE!", "TARGET CORPORATION", "RALEY'S", "GIANT", "AHOLD",
                 "LOFTHOUSE", "HARMONS", "NUCCIO'S", "MEIJER", "K&G", "KUM & GO", "BOULDER CANYON", 
                 "MAIN & GEARY", "RIVERTRAIL FOODS", "BIG Y", "SWEET SHOP USA", "REDNER'S", "SHUR FINE",
                 "HAMMOND'S", "BUBBA'S FINE FOODS", "BIG WIN", "TOO GOOD GOURMET", "VALU TIME", "CANDY SHOPPE",
                 "ORIGINAL GOURMET", "DSD MERCHANDISERS", "KROGER", "FIESTA PICO", "LONG GROVE CONFECTIONERY CO.",
                 "LINDT", "PUBLIX", "SPLURGE", "FRANKFORD", "TYRRELL'S", "BETSY ANN", "REBELL!ON", "TATE'S BAKE SHOP",
                 "SUPERIOR SNACKS", "RADZ", "HANNAFORD", "H-E-B", "JEWEL BAKE SHOP", "WILD HARVEST", "TRISCUIT", "TRIDENT", 
                 "BELVITA", "FIZZ & CO SELTZERS", "PROTEIN & PROBIOTICS", "Blue Sky Zero", "TERRY'S", "PHILADELPHIA",
                 "SHAKERS", "KOMBUCHA", "NEW ORLEANS", "RIPPLE", "KELLOGG'S", "100% JUICE", "JIMMY DEAN", "TYSON", "1/4",
                 "TABATCHNICK", "ETHINIC GOURMET", "JENNIE-O", "GORTON'S", "POLANER", "WELCH'S", "WEIS", "MRS DASH",
                 "BLUE PLATE", "PATH OF LIFE", "LITTLE SECRETS", "SPARTAN", "UDI'S", "GREAT VALUE", "YOCRUNCH", "THE LAUGHING COW",
                 "HT TRADERS", "TURKEY HILL", "SPROUT", "KASKEY'S", "CAINS", "OATS & MORE", "FOOD LION", "EMERIL'S", "NATURE'S CRUNCH", 
                 "PLSBRY", "CSCDN FARM ORG", "ANNIES HMGRWN ORG", "YOPLAIT", "KETA", "GMILLS", "Kellogg's", "NAT VLY", "CHEF-CRAFTED", 
                 "Minute Maid", "SQUEEZE & GO", "PREMIUM SPANISH", "STELLA", "NATHAN", "BRYAN", "DRAGONE", "MRS. SMITH'S",
                 "SUPERFOOD", "ROLAND", "FORD FARM", "JEFF'S NATURALS", "FULL CIRCLE", "SANTA BARBARA OLIVE CO.", "WYLWOOD", "MY ESSENTIALS",
                 "CLOVER VALLEY", "WILD THINGS", "COLONNA", "SUN OF ITALY", "SHOPRITE", "VOLPI", "GIORGIO", "FRESH FINDS", "DUNCAN HINES", "MILK MAGIC",
                 "SHOPRITE", "MARIE CALLENDERS", "BANQUET", "KID CUISINE", "ORVILLE", "SWISS MISS", "ROSARITA"]
    concatFoods = [[] for i in findFood]
    togo = []
    print(ing.shape)
    # print(findFood[0])
    # count = 0
    # for i in togo:
    #     food = np.delete(food, i - count)
    #     ing = np.delete(ing, i - count)
    #     count+=1
    # for i in findFood:
    #     food = np.append(food, i[0])
    #     ing = np.append(ing, i[1:])
    # print(ing.shape)

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
        ["*", ""],
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
                ing[ii] = None
                food[ii] = None
                canPlay = False
        for i in companies:
            if food[ii] and food[ii].find(i) != -1:
                print(food[ii])
                food[ii] = None
                ing[ii] = None
                canPlay = False
                break
        if canPlay:
            ing[ii] = ing[ii].split(", ")

    for i in range(len(food)):
        for j in range(len(findFood)):
            if food[i] and food[i].find(findFood[j]) != -1:
                print(food[i])
                if (type(ing[i]) != float and len(concatFoods[j]) < INGREDIENT_LIMIT):
                    concatFoods[j]+=ing[i]
                    # print(ing[i])
                food[i] = None
                ing[i] = None
                canPlay = False
                break
    findFood = np.array(findFood)
    # print(concatFoods[0])
    concatFoods = [list(set(i)) for i in concatFoods]
    # concatFoods = [concatFoods[i][:100] for i in range(len(concatFoods)) if len(concatFoods[i]) > 100]
    # for i in range(len(concatFoods)):
    #     if (len(concatFoods[i]) > 100): concatFoods[i] = concatFoods[i][:100]
    # print(concatFoods[0])
    # concatFoods = np.array([(list(i)) for i in concatFoods])
    # for i in concatFoods: print(i)
    # print(findFood, concatFoods)

    # print(np.array(ing).shape, concatFoods.reshape(
    #     concatFoods.shape[1],).shape)
    x = np.concatenate((np.array([i for i in food if i]), findFood), axis=0)
    # print(ing[0], concatFoods[0])
    # print(type(ing[0]), type(concatFoods[0]))  
    y1 = np.array([i for i in ing if i])
    y1.resize(y1.shape[0],)
    # print(np.array([concatFoods])[0])
    concatFoods = np.array(concatFoods)
    concatFoods.resize(concatFoods.shape[0],)
    y2 = concatFoods
    # print(y1.shape)
    # y2 = concatFoods
    y = np.concatenate((y1, y2))
    # print(y[-2:])
    print(concatFoods[0][:10])
    return [x, y]

# parsify()
