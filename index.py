'''
The Super Cool Thingy
'''

import numpy as np
import pandas as pd
processedData = "processedData"
try:
    data = pd.read_csv(F"{processedData}.csv").values()
except:
   # Import our processing code
   import processing
   data = processing.parsify()
   # Now write it into a new file.
   pd.DataFrame(np.array(data).T).to_csv(
       F"{processedData}.csv", header=False, index=False)


class Crohns():
    def __init__(self, parent="processedData.csv"):
        self.food = data[0]
        self.ing = data[1]

    def openData(self):
        li = []
        for i in self.ing:
            if (type(i) == type([])):
                li += i
        foodSet = set(li)
        # print(len(li), len(foodSet))
        self.foodToIng = {food: ing for food, ing in zip(self.food, self.ing)}
        self.foodToNum = {food: num for num, food in enumerate(foodSet)}
        self.numToFood = list(foodSet)
        # print(self.foodToIng["BAGELS"])
        print()

    def enterFood(self, food):
        pass

    def findFood(self, food):
        pass

    def mostLikely(self):
        pass


i = Crohns().openData()
