import pandas as pd
import numpy as np

def logLoss():
    pass

def sigmoid(x):
    out = 1/(1+np.exp(-x))
    return out

def softMax():
    pass

def relu():
    pass

class Net():

    def __init__(self, geometry, funclist, layers=None, weightslst=None):

        self.sizes = geometry
        self.funcs = funclist

        if weightslst:
            self.weights = weightslst
        else:
            self.weights = []

            for i in range(0,len(self.sizes)-1):
                weightarr = np.full(self.sizes[i],self.sizes[i+1],fill_value=1)
                self.weights.append(weightarr)

        if layers:
            self.layerlist = layers
        else:
            self.layerlist = []
        
            for i in range(0,len(self.sizes)):
                self.layerlist.append(Layer(self.sizes[i],self.funcs[i]))



        

        
        


class Layer():

    def __init__(self, size, func, weights):

        self.numNodes = size
        self.activation = func

        self.layerweights = weights
        
    

class Node():

    def __init__(self,biasval):
        self.bias = biasval
        self.value = 0
