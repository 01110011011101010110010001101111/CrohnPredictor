'''
The Super Cool Thingy
'''

import numpy as np
import pandas as pd
import makeAccount
processedData = "processedData"
try:
    data = pd.read_csv(F"{processedData}.csv").values()
except:
   # Import our processing code
   import processing
   data = processing.parsify()
   # Now write it into a new file.
   pd.DataFrame(np.array(data).T).to_csv(f"{processedData}.csv", header=False, index=False)


class Crohns():
    def __init__(self, parent="processedData.csv"):
        self.food = data[0]
        self.ing = data[1]
        self.ingEaten = [] # Key: [[ingName, total # of inflams, total # of times eaten, % of inflams]]

    def openData(self):
        '''
        This will open the data and create keys.
        '''
        li = []
        for i in self.ing:
            if (type(i) == type([])):
                li += i
        self.foodSet = list(set(li))  # List of all foods
        self.foodToIng = {food: ing for food, ing in zip(self.food, self.ing)} # Food to ingredient 
        self.foodToNum = {food: num for num, food in enumerate(self.foodSet)} # Food to index in food list  
        # print(self.foodToIng["BAGELS"])
        print(len(self.foodToIng), len(self.foodToNum), len(self.foodSet))

    def enterFood(self, food, inflammed):
        '''
        This will enter the data into the lsit of foods eaten.
        '''
        results = self.findFood(food) # Whether the food is in the database
        if results:
            for i in results:
                inIt = False
                for j in self.ingEaten: # If the person has already eaten the ingredient
                    if i == j[0]:
                        if inflammed: j[1]+=1 # Adds one to inflammed
                        j[2]+=1 # Adds one to total
                        j[3] = j[1]/j[2] # Updates the %
                        inIt = True
                        break
                if not inIt: # If they haven't eaten the food yet.
                    if inflammed: self.ingEaten.append([i, 1, 1, 1.0])
                    else: self.ingEaten.append([i, 0, 1, 0.0])

    def findFood(self, food):
        '''
        This function checks if the food exists within the dataset. If it does, it will return the ingredients of the food.
        '''
        if (not food in self.foodSet): 
            print(f"ERROR: {food} not found") # Will print an error
            return False
        else: 
            return self.foodToIng[food] # Returns the ingredients 
    def mostLikely(self):
        '''
        This just organises the foods based on the % of inflammations.
        '''
        self.ingEaten = sorted(self.ingEaten, reverse = True, key=lambda x:x[3])
    def filter(self):
        '''
        This will group food together based on the % of inflammations.
        '''
        self.mostLikely() # First sorts the list
        num = self.ingEaten[0][3] # Sets it to the most common
        count = 0
        self.order = [[self.ingEaten[0]]] # Holds the food based on index
        i = 1
        while i < len(self.ingEaten):
            if (self.ingEaten[i][3] == num):
                self.order[count].append(self.ingEaten[i]) # Adds it if they have the same frequency
            else:
                num = self.ingEaten[i][3]
                count+=1
                self.order.append([self.ingEaten[i]]) # Else creates a new frequency list
            i+=1
        return self.order
    def printFa(self):
        '''
        This is a nice way to print out the foods based on frequency.
        '''
        for i in self.order:
            print(f"\nOCCURING {i[0][3]} TIMES:")
            print([x[0] for x in i])


i = Crohns()
i.openData()
i.enterFood("FRENCH FRIES", 0)
i.enterFood("POPCORN", 1)
i.enterFood("SPAGHETTI", 0)
i.enterFood("WHITE BREAD", 0)
i.enterFood("TOMATO", 1)
i.enterFood("MILK", 1)
i.enterFood("YOGURT", 1)
i.filter()
i.printFa()
