import numpy as np
import matplotlib.pyplot as plt
import scipy as sp


def f(x):
    return np.exp(-x) - x

#calcula la derivada de la funcion
def df(x):
    return -np.exp(-x) - 1
def polola2():
    a=0
    x1 = f(a)
    x2 = df(a)
    x3 = a - (x1/x2)
    while (abs((x3-a)/x3) > 0.0001):
        a=x3
        x1 = f(a)
        x2 = df(a)
        x3 = a - (x1/x2)
    print(x3)

