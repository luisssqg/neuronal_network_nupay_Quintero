import numpy as np

def relu(x):
    """Función de activación ReLU"""
    return np.maximum(0, x)

def relu_derivative(x):
    """Derivada de la función ReLU"""
    return np.where(x > 0, 1, 0)

