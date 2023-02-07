#encontrar la solucion de una ecuacion de segundo grado
# Dante Alejandro Alegria Romero
#Andrea Balandran Felix
#26-01-2023 y 27-01-2023

import math
import time 
print("Resolver ecuacion de segundo grado")
print("ax^2+bx+c=0")
def operacion():
    #Pedimos los valores de a, b y c
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))
    start_time = time.time()
    if a == 0:
        print("No es una ecuacion de segundo grado debido a que si el coeficiente a es 0 es lineal")
    else:
        #Guardo en una variable lo que se hace dentro de la raiz
        d = b*b - 4*a*c
        #Si d es menor a 0 no tiene solucion real
        if d < 0:
            print("No tiene solucion real por que la raiz es negativa")
        #Si d es igual a 0 tiene una solucion solamente
        elif d == 0:
            x = -b/(2*a)
            print("Solucion unica: ", x)
        #Si d es mayor a 0 tiene dos soluciones y las resolvemos
        else:
            x1 = (-b + math.sqrt(d))/(2*a)
            x2 = (-b - math.sqrt(d))/(2*a)
            print("Soluciones: ", x1, " y ", x2)
    print("tiempo de ejecucion: %s seconds" % (time.time() - start_time))
    decision = input("Desea resolver otra ecuacion? (s/n): ")
    if decision == "s":
        operacion()
    else:
        print("Hasta luego")
#aqui ejecuta
operacion()