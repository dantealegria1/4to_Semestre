import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from falsoPunto import polola1
from Newton import polola2
from Newton import df
from puntofijo2 import polola3
import os

def f(x):
    return np.exp(-x) - x

fx = lambda x: np.exp(-x) - x
gx = lambda x: np.exp(-x)

os.system("cls")

print("Metodo de falsa posicion")
print(polola1())
print("Metodo de Newton")
print(polola2())
print("Metodo de punto fijo")
print(polola3())

diferencia = abs(polola1() - polola2())
print("La diferencia entre los metodos de falsa posicion y Newton es: ", diferencia)