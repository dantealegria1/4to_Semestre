#Comparacion de algoritmos para resolver ecuaciones de segundo grado
#Dante Alejandro Alegria Romero
#Andrea Margarita Balandran Felix


import math
import time 
import random

#pido los valores iniciales (en este caso estaticos)
print("Resolver ecuacion de segundo grado")
print("ax^2+bx+c=0")
a = 1
b = 1
c = -6
def operacion():
    #Pedimos los valores de a, b y c
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

#Iniciamos el contador de tiempo
start_time = time.time()
#Ejecutamos 10000 veces la operacion
for i in range (0, 10000):
    operacion()
#El tiempo de ejecucion es el tiempo actual menos el tiempo de inicio

#dividimos el tiempo de ejecucion entre 10000 para obtener el tiempo de ejecucion de una sola operacion
polola = (time.time() - start_time)/10000
print("tiempo de ejecucion de una sola operacion: %s seconds" % polola)
print("----------------------------------------------")


def operacion_FuerzaBruta():
    #El contador sirve para saber si se encontro una solucion
    contador = 0
    #Iteramos el primer numero
    for i in range(-100, 100):
        #Iteramos el segundo numero
        for j in range(-100, 100):
            #Si la suma de los dos numeros es igual a b y la multiplicacion de los dos numeros es igual a c
            if i + j == b and i * j == c:
                #Sumamos 1 al contador
                contador = contador + 1
                break
    #Si el contador es igual a 0 no se encontro solucion
    if contador == 0:
        print("No hay solucion")

#Mismo proceso, iniciamos el contador de tiempo
start_time = time.time()
#Lo corremos 100 veces
for i in range (0, 100):
    operacion_FuerzaBruta()
#El tiempo de ejecucion es el tiempo actual menos el tiempo de inicio

#Aqui dividimos el tiempo de ejecucion entre 100 para obtener el tiempo de ejecucion de una sola operacion
polola = (time.time() - start_time)/100
print("tiempo de ejecucion de una sola operacion: %s seconds" % polola)
print("----------------------------------------------")

def operacion_random():
    #Creamos una variable booleana para saber si se encontro una solucion
    resultado = False
    #Creamos un contador para saber si se llego al limite de iteraciones
    contador = 0
    #Mientras no se encuentre una solucion y no se llegue al limite de iteraciones
    while resultado == False:
        #Generamos dos numeros aleatorios
        i = random.randint(-100, 100)
        j = random.randint(-100, 100)
        #Si la suma de los dos numeros es igual a b y la multiplicacion de los dos numeros es igual a c
        if i + j == b and i * j == c:
            resultado = True
        #Si se llega al limite de iteraciones
        if contador == 4000:
            #Directamente decimos que es falso y se sale del while
            resultado = True
        #cada vuelta suma 1 al contador
        contador = contador + 1

#Mismo proceso, iniciamos el contador de tiempo
start_time = time.time()
for i in range (0, 100):
    operacion_random()
#El tiempo de ejecucion es el tiempo actual menos el tiempo de inicio

#Aqui dividimos el tiempo de ejecucion entre 100 para obtener el tiempo de ejecucion de una sola operacion
polola = (time.time() - start_time)/100
print("tiempo de ejecucion de una sola operacion: %s seconds" % polola)
print("----------------------------------------------")


#Comentarios
#FORMULA GENERAL
#La formula general es la forma mas eficiente de resolver una ecuacion de segundo grado
#ya que solo se necesita hacer una raiz cuadrada y una division, no es necesario iterar o
#generar mas numeros inecesarios, aprovechando la capacidad de la computadora de hacer
#operaciones matematicas rapidamente. restricciones ninguna, su uso de recursos es minimo

#FUERZA BRUTA
#La fuerza bruta es una forma de resolver un problema iterando todos los posibles
#valores que puede tomar una variable, en este caso se itero dos variables, i y J
#el problema del mismo es que como puede ser su primer iteracion el resultado final
#como puede ser la ultima, tomando el promedio que sacamos sigue siendo por bastante diferencia
#mas lento que la formula general. Restricciones: en caso de numeros mas grandes se tardaria
#mucho mas en encontrar la solucion, ya que no podemos iterar infinitamente, aun asi 
#sacrificamos bastantes recursos de la computadora para encontrar la solucion

#RANDOM
#El random es una forma de resolverlo, a diferencia del fuerza bruta no itermos sino que 
#randomizamos los valores dentro del rango establecido Restricciones: Bastantes
#ya que incluive para los casos mas simples se tarda mucho mas que la fuerza bruta si quiera
#ya que las probabilidades de que los numeros aleatorios sean los correctos son muy bajas
#y aun menos debido al hecho de que  las permutaciones se pueden repetir, por lo que tuvimos que
#agregar un contador para que no se iterara infinitamente, con un tope de 4000 iteraciones
#aun asi no encontrando soluciones en el tiempo establecido, uso de memoria y procesamiento
#bastante alto, no recomendaria su uso para ningun caso

#CONCLUSION
#La formula general es la forma mas eficiente de resolver este problema, ya que no se necesita
#iterar, ni generar numeros aleatorios, solo se necesita hacer una raiz cuadrada y una division