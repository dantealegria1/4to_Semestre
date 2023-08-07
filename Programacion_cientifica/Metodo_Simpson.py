#Materia: Programacion Cientifica
#9/06/2023
#Dante Alejandro Alegira Romero
#Andrea Margarita Balandran Felix
#Diego Alberto Aranda González

#Regla de Simpson:
#El método de integración de Simpson divide el intervalo [a, b] en subintervalos de igual longitud
#y utiliza polinomios de segundo grado para aproximar la función en cada subintervalo.
#Luego, aplica la fórmula de Simpson para calcular la suma ponderada de los valores de la función
#en los extremos y puntos medios de los subintervalos, obteniendo así una aproximación de la integral.
#La fórmula de Simpson es una regla de integración numérica que aproxima el valor de una integral definida
#mediante la suma de polinomios de segundo grado. Fue descubierta por Thomas Simpson en 1743.

#----------------------------------------------------------------------------------
#iportamos la libreria math para para poder usar las operaciones matematicas 
#importamos la libreria time para poder calcular el tiempo de ejecucion
#Asignamos los valores de el limite inferior, superior y el numero de intervalos
#Calculamos el valor de la variable que tomamos como h
#El arreglo lo creamos para guardar los valores de x0,x1,x2,x3,x4...
#Primero agregamos el limite inferior por que es nuestro punto de partida
#Despues agregamos los valores de x1,x2,x3,x4... hasta llegar al limite superior
#Agregamos el valor anterior mas el valor de h

import math
import time
#1,2,4 Es lo que estaba
Limite_inferior = int(input("Ingresa el limite inferior: "))
Limite_superior = int(input("Ingresa el limite superior: "))
n = int(input("Ingresa el numero de intervalos: "))
h = (Limite_superior - Limite_inferior) / n
array = []
array.append(Limite_inferior)
for i in range(1, n + 1):
    array.append(array[i - 1] + h)    

#----------------------------------------------------------------------------------
#Definimos la funcion que vamos a integrar
#Ejemplo de como se usa la libreria math
#la funcion que estaba era: 1/(x+1)**2

def f(x):
    return eval(user_function)

# Solicitar al usuario que ingrese la función
user_function = input("Ingrese la función: ")

#----------------------------------------------------------------------------------
#Definimos la funcion que calcula la integral
#Inicializamos una variable suma en 0
#Creamos un for que acabe cuando llegue al valor establecido por n iniciando desde 1
#OJO, el valor inicio es 1 por que x0 se tomara despues, 
# y hasta n por que queremos que se detenga 1 antes de llegar al limite superior
#Si el valor de i es par se multiplica por 2 y se suma a la variable suma
#Si el valor de i es impar se multiplica por 4 y se suma a la variable suma
#Se suma el valor de la variable suma mas el valor de f(x0) y f(xn)
#Regresamos el valor de la integral multiplicado por h/3

def Simpson():

    suma = 0   
    for i in range(1, n):
        if i % 2 == 0:
            suma = suma + 2 * f(array[i])
        else:
            suma = suma + 4 * f(array[i])
    suma = suma + f(array[0]) + f(array[n]) 
    return (h / 3) * suma

#------------------------ 
#Inicializar el tiempo de ejecución
#Ejecutar el código 500 veces sin imprimir los resultados
#Detener el tiempo de ejecución
#Calcular el tiempo de ejecución promedio 
#Dividimos el tiempo de ejecución entre 500 para obtener el tiempo promedio
#Imprimimos el tiempo promedio de ejecución

start_time = time.time()
for _ in range(500):
    Simpson()
end_time = time.time()
execution_time = end_time - start_time
print("Tiempo de ejecución promedio: ", execution_time / 500)

#---------------------------------------------------------------------------------- 
#Imprimimos el resultado de la integral

print("El resultado de la integral es: ", Simpson())

    