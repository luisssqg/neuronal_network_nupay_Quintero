import numpy as np

def tanh(x):
    """Función de activación TanH"""
    return np.tanh(x)

def tanh_derivative(x):
    """Derivada de la función TanH"""
    return 1 - np.tanh(x) ** 2


