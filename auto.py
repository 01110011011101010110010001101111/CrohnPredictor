import numpy as np
import pandas as pd
import torch
import torch.nn
# from torch.autograd import Variable

movies = pd.read_csv('ml-1m/movies.dat', sep='::',
                     header=None, engine='python', encoding='latin-1')
# Just to do stuff with the weird input file

users = pd.read_csv('ml-1m/users.dat', sep='::', header=None,
                    engine='python', encoding='latin-1')

ratings = pd.read_csv('ml-1m/ratings.dat', sep='::',
                      header=None, engine='python', encoding='latin-1')

# print(movies, users, ratings)

trainingSet = np.array(pd.read_csv(
    'ml-100k/u1.base', delimiter='\t'), dtype='int')
print(trainingSet)
testSet = np.array(pd.read_csv('ml-100k/u1.test', delimiter='\t'), dtype='int')
print(testSet)

totalUsers = int(max(max(trainingSet[:, 0]), max(testSet[:, 0])))
# Num of users; max movie id
totalMovies = int(max(max(trainingSet[:, 1]), max(testSet[:, 1])))

print(totalUsers, totalMovies)


def parse(arr):
    # Basically makes an array of users x movies
    data = []
    for i in range(1, totalUsers+1):
        movies = arr[:, 1][arr[:, 0] == i]
        # All movies ids if id == 1 or whatever the use number is
        ratings = arr[:, 2][arr[:, 0] == i]
        usrRate = np.zeros(totalMovies)
        usrRate[movies - 1] = ratings
        # For zero-indexing...
        data.append(list(usrRate))
    return data


# print(parse(trainingSet))
# print(parse(testSet))

# Tensors == array of a single data type
# Like a PyTorch array...
# Same thing with TF

trainingSet = torch.FloatTensor(parse(trainingSet))
testSet = torch.FloatTensor(parse(testSet))

'''
We're going to make a subclass of torch.nn!
'''


class StackedAutoEncoder(torch.nn.Module):  # This is for inheritance!
    # Will have several layers...
    def __init__(self, ):
        # Use super to get inherited functions
        super(StackedAutoEncoder, self).__init__()
        # Parameters: class, init function
        layer1Neurons = 20
        layer2Neurons = 10
        self.lyr1 = torch.nn.Linear(
            totalMovies, layer1Neurons)  # From the super class
        # Parameters: Number of movies, nodes / features in first hidden layer
        # Parameters: neurons[layer-1], neurons[layer]
        self.lyr2 = torch.nn.Linear(
            layer1Neurons, layer2Neurons)
        self.fullyConnectedLayer3 = torch.nn.Linear(
            layer2Neurons, layer1Neurons)
        self.fullyConnectedLayer4 = torch.nn.Linear(layer1Neurons, totalMovies)
        # Those are our layers...
        self.activation = torch.nn.Sigmoid()  # Sigmoid function

    def forwardPropagation(self, inputVector):
        '''
        We'll encode it two and decode it twice.
        '''
        predictedRating = self.activation(self.fullyConnectedLayer1(
            inputVector))  # Activates the neurons of the input as part of layer one
        # value is the encoded vector!!!
        predictedRating = self.activation(
            self.fullyConnectedLayer2(predictedRating))
        # Another encoder
        predictedRating = self.activation(
            self.fullyConnectedLayer3(predictedRating))
        # Now we're decoding!
        # No need for activation as it is the output
        predictedRating = self.fullyConnectedLayer4(predictedRating)
        # Final decoding!!!
        return predictedRating


sae = StackedAutoEncoder()

criterion = torch.nn.MSELoss()
optimiser = torch.optim.RMSprop(sae.parameters(), lr=0.01, weight_decay=0.5)

# Super awesome PyTorch stuff!
epochs = 200
for epoch in range(1, epochs+1):  # Each epoch...
    trainingLoss = 0
    # Then find the number of users who rated at least one movie to keep memory efficient
    s = 0.  # Makes s a float for the root mean square error; num of users who rated at least 1 movie
    for user in range(totalUsers):
        inp = torch.autograd.Variable(trainingSet[user]).unsqueeze(
            0)  # Creates a batch of a single input vector
        tar = inp.clone()
        if ((torch.sum(tar.data) > 0) > 0):
            output = sae.forwardPropagation(inp)
            # print(inp, output)
            tar.require_grad = False  # Does not compute a gradient with respect to the target
            # We can say that if there's no ans, then it shouldn't change the loss function
            output[tar == 0] = 0
            loss = criterion(output, tar)
            # All movies with non-zero ratings
            meanCorrector = totalMovies/float(torch.sum(tar.data > 0) + 1e-10)
            loss.backward()  # + or -; picks direction
            trainingLoss += np.sqrt(loss.data * meanCorrector)
            s += 1.
            optimiser.step()  # Picks intensity of change to weights
    print(f"Epoch {epoch}\nLoss: {trainingLoss/s}")


# Super awesome PyTorch stuff!\
testingLoss = 0
# Then find the number of users who rated at least one movie to keep memory efficient
s = 0.  # Makes s a float for the root mean square error; num of users who rated at least 1 movie
for user in range(totalUsers):
    inp = torch.autograd.Variable(trainingSet[user]).unsqueeze(
        0)  # Creates a batch of a single input vector
    tar = torch.autograd.Variable(testSet[user]).unsqueeze(0)
    if ((torch.sum(tar.data) > 0) > 0):
        output = sae.forwardPropagation(inp)
        # print(inp, output)
        tar.require_grad = False  # Does not compute a gradient with respect to the target
        # We can say that if there's no ans, then it shouldn't change the loss function
        output[tar == 0] = 0
        loss = criterion(output, tar)
        # # All movies with non-zero ratings
        meanCorrector = totalMovies/float(torch.sum(tar.data > 0) + 1e-10)
        # loss.backward()  # + or -; picks direction
        testingLoss += np.sqrt(loss.data * meanCorrector)
        s += 1.
        # optimiser.step()  # Picks intensity of change to weights
print(f"Loss: {testingLoss/s}")
