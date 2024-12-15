import pandas as pd
import numpy as np

def logLoss():
    pass

def sigmoid(x):
    out = 1/(1+np.exp(-x))
    return out

def softMax(x):
    pass

def tanh(x):
    out = np.tanh(x)
    return out

def relu(x):
    out = np.where(x >= 0, x, 0)
    return out

def identity(x):
    out = x
    return out

class Net():

    '''Need input of form [layer sizes], [layer functions] to initialise.\n
        Can pass a pre-existing set of layers and weights if needed.'''

    def __init__(self, geometry, funclist, layers=None, weightslst=None):

        

        self.sizes = geometry
        self.funcs = funclist
        self.out = None
        

        if weightslst:
            self.weights = weightslst
        else:
            self.weights = []

            for i in range(0,len(self.sizes)-1):
                weightarr = np.full((self.sizes[i],self.sizes[i+1]),fill_value=1)
                self.weights.append(weightarr)

        if layers:
            self.layerlist = layers
        else:
            self.layerlist = []
        
            for i in range(0,len(self.sizes)):
                self.layerlist.append(Layer(self.sizes[i],self.funcs[i]))

        self.params = (self.sizes,self.funcs,self.layerlist,self.weights)                           # Setting params so the network can be duplicated

    def forward(self,x):                                                                            # X passed as numpy array of same dimensions as first layer
        
        if len(x) == self.sizes[0]:

            self.layerlist[0].vals = x                                                              # Set the input layer values (note arrays are horizontal vectors so the weights are determined by that)
            
            for i in range(0,len(self.layerlist)-1):                                                # Iterates over layers (excluding output layer)
                
                print(self.layerlist[i].vals)
                #print(self.weights[i])

                z = np.matmul(self.layerlist[i].vals, self.weights[i]) + self.layerlist[i+1].biases  # z = Wx + bi+1
                #print(z)
                act = self.layerlist[i].activation(z)
                print(act)
                self.layerlist[i+1].vals = act                                                       # x_i+1 = activ_i(Wx_i + b_i+1)

            self.out = self.layerlist[-1].vals


        else:
            print('incorrect input geometry for network')

    
    def backprop(self,x):
        pass
        


    def zero(self):                                                                                 # function for if I ever want to reset the network completely

        self.weights = []
        self.layerlist = []

        for i in range(0,len(self.sizes)-1):
            weightarr = np.full((self.sizes[i],self.sizes[i+1]),fill_value=1)
            self.weights.append(weightarr)
        
        for i in range(0,len(self.sizes)):
            self.layerlist.append(Layer(self.sizes[i],self.funcs[i]))


        

        
        


class Layer():

    def __init__(self, size, func):

        self.numNodes = size
        self.activation = func

        self.vals = np.full(size,fill_value=0)
        self.biases = np.full(size,fill_value=0)

    
        
    
