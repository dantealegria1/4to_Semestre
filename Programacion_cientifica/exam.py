#Dante Alejandro Alegria Romero
#Fecha: 27/02/2023
#Nombre exam.py

from Complemeto_2 import complemento_2
from Complemeto_2 import complemento_1
from Complemeto_2 import convertir_a_binario

def binario_a_decimal(numero):
    decimal = 0
    for i in range(len(numero)):
        decimal = decimal + int(numero[i]) * 2**(len(numero)-i-1)
    return decimal

def formula(n):
    #n) = 2^K - n
    if n >= 0:
        K=8
        n=n
        f=2**K-n
        binario = bin(f)
        binario = binario [2:]
        return binario
    else:
        K=8
        n=abs(n-1)
        f=2**K-n
        binario = bin(f)
        binario = binario [2:]
        return binario

def complemento_a_decimal(numero):
    if numero & (1 << 31):
        numero = ~numero + 1
        return -int(numero)
    else:
        return int(numero)
    
def resta_binaria(a):
    if a>=0:
        a=complemento_1(a)
        #restamos 1 al numero binario
        a = int(a, 2) - 1
        #lo convertimos a binario
        a = convertir_a_binario(a)
        #lo convertimos a decimal
        a=complemento_a_decimal(int(a,2))
        a=255-a
    else:
        #convierto de binario a decimal
        numero=convertir_a_binario(a)
        decimal = 0
        for i in range(len(numero)):
            decimal = decimal + int(numero[i]) * 2**(len(numero)-i-1)
        a=decimal*-1
    return a

def main():
    #menu  
    print("1) Metodo 1")
    print("2) Metodo 2")
    print("3) Metodo 3")
    print("4) Salir")
    print("------------------")
    opcion = int(input("Ingresa una opcion: "))
    while opcion != 4:
        if opcion == 1:
            numero = int(input("Ingresa un numero: "))
            print("El complemento es: ", complemento_1(numero)," en c2 -->",resta_binaria(numero)," en decimal")
            print("Metodo tradicional donde sacamos el complemento de 1 y le restamos 1")
            print("------------------")
        elif opcion == 2:
            numero = int(input("Ingresa un numero: "))
            print("El complemento es: ", complemento_2(numero)," en c2 -->",resta_binaria(numero)," en decimal")
            print("Metodo Inverso donde volteamos los bits y le sumamos 1")
            print("------------------")
        elif opcion == 3:
            numero = int(input("Ingresa un numero: "))
            print("El complemento es: ", formula(numero)," en c2 -->",resta_binaria(numero)," en decimal")
            print("Metodo Formula 2^K-n")
            print("------------------")
        else:
            print("Opcion invalida")
        print("1) Metodo 1")
        print("2) Metodo 2")
        print("3) Metodo 3")
        print("4) Salir")
        opcion = int(input("Ingresa una opcion: "))
        print("------------------")
    print("Adios")

if __name__ == "__main__":
    main()



