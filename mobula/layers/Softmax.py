from .Layer import *

class Softmax(Layer):
    def __init__(self, model, *args, **kwargs):
        Layer.__init__(self, model, *args, **kwargs)
        self.axis = kwargs.get("axis", 1) # N,C,H,W
    def reshape(self):
        self.Y = np.zeros(self.X.shape)
    def forward(self):
        e = np.exp(self.X - np.max(self.X, axis = self.axis, keepdims = True))
        s = np.sum(e, axis = self.axis, keepdims = True)
        self.Y = e / s
    def backward(self):
        self.dX = np.multiply(self.dY, self.Y - np.square(self.Y))
