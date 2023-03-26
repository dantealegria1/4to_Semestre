import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.exp(-x) - x

def polola1():
    a=0
    b=1
    x1 = f(a)
    x2 = f(b)
    error = 1e-4
    if x1*x2 > 0:
        print("No hay raiz en el intervalo")
    else:
        x = (a*f(b) - b*f(a))/(f(b) - f(a))
        x0 = f(x)
        while abs(x0) > error:
            if x1*x0 < 0:
                b = x
            else:
                a = x
            x = (a*f(b) - b*f(a))/(f(b) - f(a))
            x0 = f(x)
        print("La raiz es: ", x)

polola1()








    