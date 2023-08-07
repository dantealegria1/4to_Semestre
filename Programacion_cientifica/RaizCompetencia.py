import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from falsoPunto import polola1
from Newton import polola2
from Newton import df
from puntofijo2 import polola3
import os
from scipy.optimize import fsolve

#Son las funciones para los metodos
def f(x):
    return np.exp(-x) - x

fx = lambda x: np.exp(-x) - x
gx = lambda x: np.exp(-x)

#Esta parte es por que me imprime una vez extra el resultado jaja
os.system("cls")

def graficar():
    x = np.linspace(-5, 5, 100)

    # Evaluar la función en los valores x
    y = f(x)

    # Encontrar la raíz de la función
    root = fsolve(f, 0)

    # Graficar la función y la raíz
    plt.plot(x, y)
    plt.axhline(y=0, color='k')
    plt.axvline(x=root, color='r')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

def menu():
    print("1. Graficar")
    print("2. Metodo de falsa posicion")
    print("3. Metodo de Newton")
    print("4. Metodo de punto fijo")
    print("5. Salir")
    opc=int(input("Ingrese una opcion: "))
    if opc==1:
        graficar()
        menu()
    elif opc==2:
        print("metodo de falsa posicion")
        print(polola1())
        menu()
    elif opc==3:
        print("metodo de Newton")
        print(polola2())
        menu()
    elif opc==4:
        print("metodo de punto fijo")
        print(polola3())
        menu()
    elif opc==5:
        print("Adios")
    else:
        print("Opcion incorrecta")
        menu()


menu()