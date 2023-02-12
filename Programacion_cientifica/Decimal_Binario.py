#De decimal a binario
#Dante Alejandro Alegria Romero
#08/02/2023

#Funcion para convertir de decimal a binario
def decimal_binario(numero):
    binario = ""
    while numero > 0:
        binario = str(numero%2) + binario
        numero = numero // 2
    return binario

print(decimal_binario(35))