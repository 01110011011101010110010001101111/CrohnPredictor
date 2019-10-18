'''
The Super Cool Thingy
'''

import numpy as np
import pandas as pd
import cluster
processedData = "processedData"
try:
    data = pd.read_csv(F"{processedData}.csv").values()
except:
   # Import our processing code
   import processing
   data = processing.parsify()
   # Now write it into a new file.
   pd.DataFrame(np.array(data).T).to_csv(f"{processedData}.csv", header=False, index=False)


class Crohns(cluster.Clusters):
    def __init__(self, parent="processedData.csv", accounts = "Accounts"):
        super()
        super().__init__(accounts)
        self.food = data[0]
        self.ing = data[1]
        self.ingEaten = [] # Key: [[ingName, total # of inflams, total # of times eaten, % of inflams]]
    
    def loginAndUpdate(self, username, password):
        if(self.login(username, password)):
            self.loginAndEnter(username, password)
            # self.login(username, password)
            self.order = self.userStat
            self.orderToEaten()
    def orderToEaten(self):
        '''
        Makes the fancy array based on % change into just an array of the ingredients eaten
        '''
        self.ingEaten = [i for j in self.order for i in j]
        # print(len(self.ingEaten))
        # print(self.ingEaten)
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
        This will enter the data into the list of foods eaten.
        '''
        results = self.findFood(food) # Whether the food is in the database; if yes, returns array
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
                    self.ingEaten.append([i, int(inflammed), 1, float(inflammed)])

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
        self.editStats(str(self.order))
        return self.order
    def printFa(self):
        '''
        This is a nice way to print out the foods based on frequency.
        '''
        for i in self.order:
            print(f"\nOCCURING IN {i[0][3]*100}%:")
            print([x[0] for x in i])

i = Crohns()
# i.addClient("IhateDairy", "password", "Dairy Hater", '[]')
i.loginAndUpdate("IhateDairy", "password")
i.openData()
# i.enterFood("MILK", True)
# i.enterFood("YOGURT", True)
# i.enterFood("PIZZA", True)
# i.enterFood("CHICKEN", False)
# i.filter()
i.printFa()
i.printPoints()
i.printPointsII()
i.KMeansPercentTotal()
i.KMeansRatio()