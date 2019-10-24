import numpy as np 
import makeAccount
import matplotlib.pyplot as plt
import base64
from io import BytesIO


class Clusters(makeAccount.CSV):
    def __init__(self, accounts = "Accounts"):
        super()
        super().__init__(accounts)
    def loginAndEnter(self, user, word):
        '''
        This logs in an initalises the array.
        '''
        self.login(user, word)
        if (self.authenticated):
            self.stuff = eval(self.getStats())
            # print(self.restrict)
            self.allCoord = np.array([np.array([x, y-x]) for j in self.stuff for ing, x, y, _ in j if ing not in self.restrict])
            self.partPercent = np.array([np.array(
                [x, percent]) for j in self.stuff for ing, x, _, percent in j if ing not in self.restrict])
            self.percentTotal = np.array(
                [np.array([y, percent]) for j in self.stuff for ing, _, y, percent in j if ing not in self.restrict])
            x = [x for j in self.stuff for ing, x, _,
                 _ in j if ing not in self.restrict]
            y = [y-x for j in self.stuff for ing, x,
                 y, _ in j if ing not in self.restrict]
            self.labels = [label for j in self.stuff for label,
                           _, _, _ in j if label not in self.restrict]

    def printPointsRatio(self):
        '''
        Type: Plots
        Y-axis: No Reaction
        X-axis: Reaction
        '''
        if (self.authenticated):
            # print(ratio)
            plt.ylabel("NO REACTION")
            plt.xlabel("REACTION")
            # print(self.allCoord)
            plt.yticks(np.arange(0, max(self.allCoord[:, 0]) + 10, 1))
            plt.xticks(np.arange(0, max(self.allCoord[:, 1]) + 10, 1))
            # plt.scatter(np.array(x), np.array(y))
            plt.scatter(self.allCoord[:, 0], self.allCoord[:, 1])
            for i, txt in enumerate(self.labels):
                # plt.annotate(txt, (x[i], y[i]))
                plt.annotate(txt, (self.allCoord[i][0], self.allCoord[i][1]))
            plt.title("Plots: Reaction, No Reaction")
            plt.show()

    def printPointsPartPercent(self):
        '''
        Type: Plots
        Y-axis: % Reactions
        X-axis: # Reactions
        '''
        if self.authenticated:
            plt.ylabel("PERCENT OF REACTIONS")
            plt.xlabel("NUM OF REACTIONS")
            plt.yticks(np.arange(0, 1.1, 0.1))
            plt.xticks(np.arange(0, max(self.partPercent[:, 1]) + 10, 1))
            # plt.scatter(np.array(x), np.array(y))
            plt.scatter(self.partPercent[:, 0], self.partPercent[:, 1])
            for i, txt in enumerate(self.labels):
                # plt.annotate(txt, (x[i], y[i]))
                plt.annotate(txt, (self.partPercent[i][0], self.partPercent[i][1]))
            plt.title("Plots: # Reactions, % Reactions")
            plt.show()
    
    def printPointsPercentTotal(self):
        '''
        Type: Plots
        Y-axis: % Reactions
        X-axis: # Observations
        '''
        if self.authenticated:
            plt.ylabel("PERCENT OF REACTIONS")
            plt.xlabel("TOTAL NUM")
            plt.yticks(np.arange(0, 1.1, 0.1))
            plt.xticks(np.arange(0, max(self.percentTotal[:, 1]) + 10, 1))
            # plt.scatter(np.array(x), np.array(y))
            plt.scatter(self.percentTotal[:, 0], self.percentTotal[:, 1])
            for i, txt in enumerate(self.labels):
                # plt.annotate(txt, (x[i], y[i]))
                plt.annotate(
                    txt, (self.percentTotal[i][0], self.percentTotal[i][1]))
            plt.title("Plots: # Observations, % Reactions")
            plt.show()

    def KMeansRatio(self):
        '''
        Type: K-Means
        Y-axis: No Reaction
        X-axis: Reaction
        '''
        if self.authenticated:
            from sklearn.cluster import KMeans as KM
            algorithm = KM(n_clusters=2)
            categories = algorithm.fit_predict(self.allCoord)
            plt.scatter(self.allCoord[categories == 0, 0], self.allCoord[categories == 0, 1], c= "green")
            plt.scatter(self.allCoord[categories == 1, 0],self.allCoord[categories == 1, 1], c="red")
            plt.scatter(algorithm.cluster_centers_[:, 0], algorithm.cluster_centers_[:, 1], c= "black", marker="*")
            for i, txt in enumerate(self.labels):
                plt.annotate(txt, (self.allCoord[i][0], self.allCoord[i][1]))
            plt.ylabel("NO REACTION")
            plt.xlabel("REACTION")
            plt.annotate("NO INFLAMMATION", algorithm.cluster_centers_[0])
            plt.annotate("CAUSES INFLAMMATION", algorithm.cluster_centers_[1])
            plt.title("K-Means: Reaction, No Reaction")
            plt.show()

    def KMeansPartPercent(self):
        '''
        Type: K-Means
        Y-axis: % Reactions
        X-axis: # Reactions
        '''
        if self.authenticated:
            from sklearn.cluster import KMeans as KM
            algorithm = KM(n_clusters=2)
            # partPercent = np.array([np.array([x, percent]) for j in self.stuff for _, x, _, percent in j])
            categories = algorithm.fit_predict(self.partPercent)
            plt.scatter(self.partPercent[categories == 0, 0],
                        self.partPercent[categories == 0, 1], c="green")
            plt.scatter(self.partPercent[categories == 1, 0],
                        self.partPercent[categories == 1, 1], c="red")
            plt.scatter(algorithm.cluster_centers_[:, 0], algorithm.cluster_centers_[
                        :, 1], c="black", marker="*")
            for i, txt in enumerate(self.labels):
                plt.annotate(
                    txt, (self.partPercent[i][0], self.partPercent[i][1]))
            plt.ylabel("PERCENT")
            plt.xlabel("NUM OF INFLAMS")
            plt.annotate("NO INFLAMMATION", algorithm.cluster_centers_[0])
            plt.annotate("CAUSES INFLAMMATION", algorithm.cluster_centers_[1])
            plt.title("K-Means: # Reactions, % Reactions")
            plt.show()

    def KMeansPercentTotal(self):
        '''
        Type: K-Means
        Y-axis: % Reactions
        X-axis: # Observations
        '''
        if self.authenticated:
            from sklearn.cluster import KMeans as KM
            algorithm = KM(n_clusters=2)
            fig = plt.figure()
            # partPercent = np.array([np.array([x, percent]) for j in self.stuff for _, x, _, percent in j])
            categories = algorithm.fit_predict(self.percentTotal)
            plt.scatter(self.percentTotal[categories == 0, 0],
                        self.percentTotal[categories == 0, 1], c="green")
            plt.scatter(self.percentTotal[categories == 1, 0],
                        self.percentTotal[categories == 1, 1], c="red")
            plt.scatter(algorithm.cluster_centers_[:, 0], algorithm.cluster_centers_[
                        :, 1], c="black", marker="*")
            for i, txt in enumerate(self.labels):
                plt.annotate(
                    txt, (self.percentTotal[i][0], self.percentTotal[i][1]))
            plt.ylabel("PERCENT")
            plt.xlabel("TOTAL")
            plt.annotate("NO INFLAMMATION", algorithm.cluster_centers_[0])
            plt.annotate("CAUSES INFLAMMATION", algorithm.cluster_centers_[1])
            plt.title("K-Means: # Observations, % Reactions")
            # plt.show()
            # mpld3.show()
            # plt.savefig()



            tmpfile = BytesIO()
            # plt.savefig('test.png')
            fig.savefig(tmpfile, format='png')
            encoded = base64.b64encode(tmpfile.getvalue())

            html = '<img src=\'data:image/png;base64,{}\'>'.format(encoded.decode("utf-8"))

            with open('KMeansPercentTotal.html', 'w') as f:
                f.write(html)
            # print(mpld3.fig_to_html())
    
    def KModesRatio(self):
        '''
        Type: K-Modes
        Y-axis: No Reaction
        X-axis: Reaction
        '''
        if self.authenticated:
            from kmodes.kmodes import KModes as KMo 
            algorithm = KMo(n_clusters=2)
            categories = algorithm.fit_predict(self.allCoord)
            print(algorithm.cluster_centroids_)
            plt.scatter(self.allCoord[categories == 0, 0],
                        self.allCoord[categories == 0, 1], c="green")
            plt.scatter(self.allCoord[categories == 1, 0],
                        self.allCoord[categories == 1, 1], c="red")
            plt.scatter(algorithm.cluster_centroids_[:, 0], algorithm.cluster_centroids_[
                        :, 1], c="black", marker="*")
            for i, txt in enumerate(self.labels):
                plt.annotate(txt, (self.allCoord[i][0], self.allCoord[i][1]))
            plt.ylabel("NO REACTION")
            plt.xlabel("REACTION")
            plt.annotate("NO INFLAMMATION", algorithm.cluster_centroids_[0])
            plt.annotate("CAUSES INFLAMMATION", algorithm.cluster_centroids_[1])
            plt.title("K-Modes: Reaction, No Reaction")
            plt.show()

    def KModePartPercent(self):
        '''
        Type: K-Modes
        Y-axis: % Reactions
        X-axis: # Reactions
        '''
        if self.authenticated:
            from kmodes.kmodes import KModes as KMo
            algorithm = KMo(n_clusters=2)
            # partPercent = np.array([np.array([x, percent]) for j in self.stuff for _, x, _, percent in j])
            categories = algorithm.fit_predict(self.partPercent)
            plt.scatter(self.partPercent[categories == 0, 0],
                        self.partPercent[categories == 0, 1], c="green")
            plt.scatter(self.partPercent[categories == 1, 0],
                        self.partPercent[categories == 1, 1], c="red")
            plt.scatter(algorithm.cluster_centroids_[:, 0], algorithm.cluster_centroids_[
                        :, 1], c="black", marker="*")
            for i, txt in enumerate(self.labels):
                plt.annotate(
                    txt, (self.partPercent[i][0], self.partPercent[i][1]))
            plt.ylabel("PERCENT")
            plt.xlabel("NUM OF INFLAMS")
            plt.annotate("NO INFLAMMATION", algorithm.cluster_centroids_[0])
            plt.annotate("CAUSES INFLAMMATION", algorithm.cluster_centroids_[1])
            plt.title("K-Modes: # Reactions, % Reactions")
            plt.show()

    def KModePercentTotal(self):
        '''
        Type: K-Modes
        Y-axis: % Reactions
        X-axis: # Observations
        '''
        if self.authenticated:
            from kmodes.kmodes import KModes as KMo
            algorithm = KMo(n_clusters=2)
            # partPercent = np.array([np.array([x, percent]) for j in self.stuff for _, x, _, percent in j])
            categories = algorithm.fit_predict(self.percentTotal)
            plt.scatter(self.percentTotal[categories == 0, 0],
                        self.percentTotal[categories == 0, 1], c="green")
            plt.scatter(self.percentTotal[categories == 1, 0],
                        self.percentTotal[categories == 1, 1], c="red")
            plt.scatter(algorithm.cluster_centroids_[:, 0], algorithm.cluster_centroids_[
                        :, 1], c="black", marker="*")
            for i, txt in enumerate(self.labels):
                plt.annotate(
                    txt, (self.percentTotal[i][0], self.percentTotal[i][1]))
            plt.ylabel("PERCENT")
            plt.xlabel("TOTAL")
            plt.annotate("NO INFLAMMATION", algorithm.cluster_centroids_[0])
            plt.annotate("CAUSES INFLAMMATION", algorithm.cluster_centroids_[1])
            plt.title("K-Modes: # Observations, % Reactions")
            plt.show()
    
    def MeanShiftRatio(self):
        '''
        Type: MeanShift
        Y-axis: No Reaction
        X-axis: Reaction
        '''
        if self.authenticated:
            from sklearn.cluster import MeanShift as MS
            algorithm = MS(bandwidth=2)
            categories = algorithm.fit_predict(self.allCoord)
            plt.scatter(self.allCoord[categories == 0, 0],
                        self.allCoord[categories == 0, 1], c="green")
            plt.scatter(self.allCoord[categories == 1, 0],
                        self.allCoord[categories == 1, 1], c="red")
            plt.scatter(algorithm.cluster_centers_[:, 0], algorithm.cluster_centers_[
                        :, 1], c="black", marker="*")
            for i, txt in enumerate(self.labels):
                plt.annotate(txt, (self.allCoord[i][0], self.allCoord[i][1]))
            plt.ylabel("NO REACTION")
            plt.xlabel("REACTION")
            plt.annotate("NO INFLAMMATION", algorithm.cluster_centers_[0])
            plt.annotate("CAUSES INFLAMMATION", algorithm.cluster_centers_[1])
            plt.title("MeanShift: Reaction, No Reaction")
            plt.show()

    def MeanShiftPartPercent(self):
        '''
        Type: MeanShift
        Y-axis: % Reactions
        X-axis: # Reactions
        '''
        if self.authenticated:
            from sklearn.cluster import MeanShift as MS
            algorithm = MS(bandwidth=2)
            categories = algorithm.fit_predict(self.partPercent)
            plt.scatter(self.partPercent[categories == 0, 0],
                        self.partPercent[categories == 0, 1], c="green")
            plt.scatter(self.partPercent[categories == 1, 0],
                        self.partPercent[categories == 1, 1], c="red")
            plt.scatter(algorithm.cluster_centers_[:, 0], algorithm.cluster_centers_[
                        :, 1], c="black", marker="*")
            for i, txt in enumerate(self.labels):
                plt.annotate(
                    txt, (self.partPercent[i][0], self.partPercent[i][1]))
            plt.ylabel("PERCENT")
            plt.xlabel("NUM OF INFLAMS")
            plt.annotate("NO INFLAMMATION", algorithm.cluster_centers_[0])
            plt.annotate("CAUSES INFLAMMATION", algorithm.cluster_centers_[1])
            plt.title("MeanShift: # Reactions, % Reactions")
            plt.show()

    def MeanShiftPercentTotal(self):
        '''
        Type: MeanShift
        Y-axis: % Reactions
        X-axis: # Observations
        '''
        if self.authenticated:
            from sklearn.cluster import MeanShift as MS
            algorithm = MS(bandwidth=2)
            categories = algorithm.fit_predict(self.percentTotal)
            plt.scatter(self.percentTotal[categories == 0, 0],
                        self.percentTotal[categories == 0, 1], c="green")
            plt.scatter(self.percentTotal[categories == 1, 0],
                        self.percentTotal[categories == 1, 1], c="red")
            plt.scatter(algorithm.cluster_centers_[:, 0], algorithm.cluster_centers_[
                        :, 1], c="black", marker="*")
            for i, txt in enumerate(self.labels):
                plt.annotate(
                    txt, (self.percentTotal[i][0], self.percentTotal[i][1]))
            plt.ylabel("PERCENT")
            plt.xlabel("TOTAL")
            plt.annotate("NO INFLAMMATION", algorithm.cluster_centers_[0])
            plt.annotate("CAUSES INFLAMMATION", algorithm.cluster_centers_[1])
            plt.title("MeanShift: # Observations, % Reactions")
            plt.show()

    def setTheory(self):
        '''
        Experiment for now
        '''
        if self.authenticated:
            print(self.percentTotal)
            
        '''
        Okay. Let's start with a threshold value. I don't want any ingredients under x to be counted.
        '''
        


i = Clusters()
i.loginAndEnter("SHREYA", "password")
# i.printPointsRatio()
# i.printPointsPartPercent()
# i.addRestriction("CITRIC ACID")
# i.printPointsPercentTotal()
# i.KMeansRatio()
# i.KMeansPartPercent()
i.KMeansPercentTotal()
# i.MeanShiftRatio()
# i.KMeansPartPercent()
# i.MeanShiftPercentTotal()
# i.KModesRatio()
# i.KMeansPartPercent()
# i.KModePercentTotal()
# i.handsOn()
