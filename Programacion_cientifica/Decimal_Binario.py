#De decimal a binario
#Dante Alejandro Alegria Romero
#08/02/2023

#Funcion para convertir de decimal a binario
#todo: / signfica cambio de linea
#Como funciona la funcion:
#Primero separamos la parte fraccioanria y la entera
#todo: Entero = int(numero) / Fraccion = numero - Entero 
#Luego creamos una lista vacia para guardar los numeros binarios
#Convertimos la parte entera a binario
#todo: binario1 = bin(Entero) / binario1 = binario1[2:]
#Luego creamos un ciclo while para convertir la parte fraccional
#Que lo que hace es multiplicar la parte fraccionaria *2
#todo: Fraccion = Fraccion * 2
#Hacemos un if que se refiere a que si la parte fraccional es mayor o igual a 1
#le sumamos un 1 a la lista y a la parte fraccionaria le restamos 1
#todo: if Fraccion >= 1: / binario = binario + "1" / Fraccion = Fraccion - 1
#Si no se cumple la condicion anterior, le sumamos un 0 a la lista 
#y se repite el proceso hasta que la parte fraccional sea 0

def decimal_binario(numero):
    Entero = int(numero)
    Fraccion = numero - Entero
    binario = ""
    binario1 = bin(Entero)
    binario1 = binario1[2:]
    while Fraccion > 0:
        Fraccion = Fraccion * 2
        if Fraccion >= 1:
            binario = binario + "1"
            Fraccion = Fraccion - 1
        else:
            binario = binario + "0"
    print(binario1 + "." + binario)
    return binario1 + "." + binario


def main():
    numero = float(input("Ingrese un numero: "))
    decimal_binario(numero)

if __name__ == "__main__":
    main()