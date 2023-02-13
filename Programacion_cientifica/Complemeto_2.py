#Tarea 3 Programar la representación de los 
# números enteros (positivos y negativos) en complemento a 2
#Dante Alejandro Alegria Romero
#Fecha: 13/02/2023

import time

#Aqui lo convertimos a binario   de toda la vida
#Quite el bin por que quedaba mas ojete
def convertir_a_binario(numero):
    binario = ''
    if numero < 0:
        numero = abs(numero)
    while numero > 0:
        binario = str(numero % 2) + binario
        numero = numero // 2
    #La diferencia es que ahora lo llenamos con ceros a
    #  la izquierda para que sea de 8 bits
    for i in range (8-len(binario)):
        binario = '0' + binario
    return binario

def complemento_1(numero):
    #Lo convertimos a binario
    binario = convertir_a_binario(numero)
    #creamos el complemento
    complemento = ''
    #Si es positivo, solo invertimos los bits
    if numero > 0:
        for i in range(len(binario)):
            if binario[i] == '0':
                complemento = complemento + '1'
            else:
                complemento = complemento + '0'
        #sumamos 1 al complemento de manea binaria
        #por eso ponemos el 2 en la funcion
        complemento = int(complemento, 2) + 1
        #lo convertimos a binario
        complemento = convertir_a_binario(complemento)
    else:
        #Si es negativo, lo convertimos a positivo 
        #El abs es de absolute value
        numero = abs(numero-1)
        #lo convertimos a binario
        complemento = convertir_a_binario(numero)
        #Diferencia es que en vez de sumar le restamos uno, por que
        #el numero es negativo es igual a el numero binario de n+1 volteado lol
        complemento = int(complemento, 2) - 1
        complemento = convertir_a_binario(complemento)
    return complemento

def complemento_2(numero):
    #directamente mandamos a llamar a la primera funcion pa no escribir
    if numero >= 0:
        complemento = complemento_1(numero)
    else:
        #Si es negativo, lo convertimos a positivo y le restamos uno
        complemento = complemento_1(abs(numero-1))
        #lo invertimos y es todo
        for i in range(len(complemento)):
            if complemento[i] == '0':
                complemento = complemento[:i] + '1' + complemento[i+1:]
            else:
                complemento = complemento[:i] + '0' + complemento[i+1:]
    return complemento

#Esta funcion es para comparar los dos metodos si es que hay algun error
#avisa y te dice en que numero esta el error
def correr_pruebas():
    contador = 0
    for i in range(-128, 128):
        if complemento_1(i) != complemento_2(i):
            print("Error en el numero: ", i)
            print("El complemento 1 es: ", complemento_1(i))
            print("El complemento 2 es: ", complemento_2(i))
            contador = contador + 1
    print("Pruebas terminadas con ", contador, " errores")

#La funcion main es para comparar el tiempo de ejecucion de los dos metodos y los comparamos
#igual a como lo hicimos la vez de la solucion de metodos de resolver ecuaciones
def main():
    #compara el tiempo de ejecución de los dos métodos
    start_time = time.time()
    for i in range(1000):
        complemento_1(i)
    print("El tiempo de una sola ejecucion es de: %s seconds"
    % ((time.time() - start_time)/1000))
    print("--------------------------------------------------")

    start_time = time.time()
    for i in range(1000):
        complemento_2(i)
    print("El tiempo de una sola ejecucion es de: %s seconds"
    % ((time.time() - start_time)/1000))

if __name__ == '__main__':
    main()
    correr_pruebas()

#El complemento 2 yo lo vi con la formula de que si es positivo
#lo convertimos a binario, lo volteamos y le sumamos uno y ya quedo
#pero si es negativo, lo convertimos a positivo, le restamos uno, 
#le sacamos el binario y ya quedo

#Ejemplo
#me dan el numero 3 que en binario es 00000011
#Si lo volteo es 11111100
#Si le sumo uno es 11111101 y eso es todo

#Si me dan el numero -3 
#Lo hago positivo le sumo uno  que da 4
#Le saco el binario que da 00000100
#Lo vuelvo a voltear que da 11111011
#le sumo uno que da 11111100 
#Lo vuelvo a voltear que da 00000011