#Metodo de Falso punto
#Dante Alejandro Alegria Romero
import numpy as np
import matplotlib.pyplot as plt
#Paso 1: Evaluar f(a) y f(b)
def f(x):
    y=np.cos(x)
    return y

def valores():
    a=float(input("Ingrese el valor de a: "))
    b=float(input("Ingrese el valor de b: "))
    return a,b
