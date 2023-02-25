#programa que convierte base 10 a base IEEE754
#Dante Alejandro ALegria Romero
#Fecha: 21/02/2022

#funcion que convierte en binario
def binario(numero):
    #convierto a positivo el numero
    if numero < 0:
        numero = numero * -1
    #separar la parte entera y decimal
    parteEntera = int(numero)
    parteDecimal = numero - parteEntera
    #convertir la parte entera a binario
    binarioEntero = ""
    while parteEntera > 0:
        binarioEntero = str(parteEntera % 2) + binarioEntero
        parteEntera = parteEntera // 2
    #convertir la parte decimal a binario
    binarioDecimal = ""
    while parteDecimal > 0:
        parteDecimal = parteDecimal * 2
        if parteDecimal >= 1:
            binarioDecimal = binarioDecimal + "1"
            parteDecimal = parteDecimal - 1
        else:
            binarioDecimal = binarioDecimal + "0"
    #unir la parte entera y decimal
    binario = binarioEntero + "." + binarioDecimal
    return binario

def baseIEEE754(numero):
    binario2 = binario(numero)
    binario3 = binario2
    print("binario", binario2)
    #normalizar el numero
    #recorremos el punto decimal hasta que sea 1
    punto = binario2.find(".")
    #encontramos el primer 1
    primer1 = binario2.find("1")
    #normalizamos el numero poniendo el punto despues del 1
    binario2 = binario2.replace(".", "")
    binario2 = binario2[:primer1+1] + "." + binario2[primer1+1:]
    print("binario normalizado", binario2)
    #encontrar el exponente
    punto_inicial = binario3.find(".")
    punto_normalizado = binario2.find(".")
    exponente = punto_inicial - punto_normalizado
    print("exponente", exponente)
    Exponente_sesgado = 127 + exponente
    Exponente_sesgado_binario = binario(Exponente_sesgado)
    Exponente_sesgado_binario = Exponente_sesgado_binario.replace(".", "")
    
    print("exponente sesgado", Exponente_sesgado_binario)
    signo = 0
    if numero < 0:
        signo = 1
    print("signo", signo)
    #encontrar la mantisa
    mantisa = binario2[2:]
    for i in range(23 - len(mantisa)):
        mantisa = mantisa + "0"
    print("mantisa", mantisa)
    #encontrar el numero en base IEEE754
    convertido = str(signo) +"-"+ Exponente_sesgado_binario+"-" + mantisa
    print("numero convertido", convertido)
    return convertido

baseIEEE754(127)
