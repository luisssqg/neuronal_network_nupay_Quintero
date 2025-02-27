import numpy as np

def sigmoid(x):
    """Función de activación Sigmoide"""
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    """Derivada de la función Sigmoide"""
    s = sigmoid(x)
    return s * (1 - s)
