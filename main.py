import numpy as np
import matplotlib.pyplot as plt
from src.sigmoid import sigmoid, sigmoid_derivative
from src.relu import relu, relu_derivative
from src.tanh import tanh, tanh_derivative

def plot_function(x, func, title):
    """Grafica una función de activación"""
    y = func(x)
    plt.plot(x, y, label=title)
    plt.title(title)
    plt.legend()
    plt.grid()

def main():
    x = np.linspace(-5, 5, 100)
    plt.figure(figsize=(12, 6))
    
    plt.subplot(2, 3, 1)
    plot_function(x, sigmoid, "Sigmoid")
    plt.subplot(2, 3, 2)
    plot_function(x, relu, "ReLU")
    plt.subplot(2, 3, 3)
    plot_function(x, tanh, "TanH")
    
    plt.subplot(2, 3, 4)
    plot_function(x, sigmoid_derivative, "Sigmoid Derivative")
    plt.subplot(2, 3, 5)
    plot_function(x, relu_derivative, "ReLU Derivative")
    plt.subplot(2, 3, 6)
    plot_function(x, tanh_derivative, "TanH Derivative")
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()

