import numpy as np 
import makeAccount
import matplotlib.pyplot as plt


class Clusters(makeAccount.CSV):
    def __init__(self, accounts = "Accounts"):
        super()
        super().__init__(accounts)
        # print("UNDER HERE")
        # print(eval(i.getStats()))
        # print(self.allCoord)
    def loginAndEnter(self, user, word):
        self.login(user, word)
        self.stuff = eval(self.getStats())
        # print([[x, y-x] for _, x, y, _ in stuff[0]])
        self.allCoord = np.array([np.array([x, y-x]) for j in self.stuff for _, x, y, _ in j])
    def printPoints(self):
        x = [x for j in self.stuff for _, x, y, _ in j]
        y = [y-x for j in self.stuff for _, x, y, _ in j]
        self.labels = [label for j in self.stuff for label, _, _, _ in j]
        # print(ratio)
        plt.ylabel("NO REACTION")
        plt.xlabel("REACTION")
        plt.yticks(np.arange(0, max(self.allCoord[:, 0]) + 10, 1))
        plt.xticks(np.arange(0, max(self.allCoord[:, 1]) + 10, 1))
        # plt.scatter(np.array(x), np.array(y))
        plt.scatter(self.allCoord[:, 0], self.allCoord[:, 1])
        for i, txt in enumerate(self.labels):
            # plt.annotate(txt, (x[i], y[i]))
            plt.annotate(txt, (self.allCoord[i][0], self.allCoord[i][1]))
        plt.show()
    def KMeans(self):
        from sklearn.cluster import KMeans as KM
        algorithm = KM(n_clusters=2)
        categories = algorithm.fit_predict(self.allCoord)
        plt.scatter(self.allCoord[categories == 0, 0], self.allCoord[categories == 0, 1], c= "green")
        plt.scatter(self.allCoord[categories == 1, 0],self.allCoord[categories == 1, 1], c="red")
        plt.scatter(algorithm.cluster_centers_[:, 0], algorithm.cluster_centers_[:, 1], c= "black", marker="*")
        for i, txt in enumerate(self.labels):
            plt.annotate(txt, (self.allCoord[i][0], self.allCoord[i][1]))
        plt.annotate("NO INFLAMMATION", algorithm.cluster_centers_[0])
        plt.annotate("CAUSES INFLAMMATION", algorithm.cluster_centers_[1])
        plt.show()


i = Clusters()
i.loginAndEnter("SHREYA", "password")
i.printPoints()
i.KMeans()
