#dos numeros que sumados den b y multiplicados c
#Dante Alejandro Alegria Romero
#Andrea Balandran Felix
#30-01-2023

import random
import time

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

def operacion_FuerzaBruta():
    contador = 0
    for i in range(-100, 100):
        for j in range(-100, 100):
            if i + j == b and i * j == c:
                print("Los numeros son: ", i, " y ", j)
                contador = contador + 1
                break
    if contador == 0:
        print("No hay solucion")

def operacion_random():
    resultado = False
    contador = 0
    while resultado == False:
        i = random.randint(-100, 100)
        j = random.randint(-100, 100)
        if i + j == b and i * j == c:
            print("Los numeros son: ", i, " y ", j)
            print("Se encontro en el intento: ", contador)
            resultado = True
        if contador == 4000:
            print("No hay solucion despues de 4000 intentos")
            resultado = True
        contador = contador + 1

print("Fuerza Bruta")
operacion_FuerzaBruta()
print("-------------------")
print("Random")
operacion_random()

print("tiempos de ejecucion")
start_time = time.time()
operacion_FuerzaBruta()
print("Fuerza Bruta: %s seconds" % (time.time() - start_time))
start_time = time.time()
operacion_random()
print("Random: %s seconds" % (time.time() - start_time))

