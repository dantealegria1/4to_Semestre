# Algoritmo de punto fijo
# [a,b] intervalo de búsqueda
# error = tolera

import numpy as np

def puntofijo(gx,a,tolera, iteramax = 15):
    i = 1 # iteración
    b = gx(a)
    tramo = abs(b-a)
    while(tramo>=tolera and i<=iteramax ):
        a = b
        b = gx(a)
        tramo = abs(b-a)
        i = i + 1
    respuesta = b
    
    # Validar respuesta
    if (i>=iteramax ):
        respuesta = np.nan
    return(respuesta)

# PROGRAMA ---------

# INGRESO
fx = lambda x: np.exp(-x) - x
gx = lambda x: np.exp(-x)

a = float(input("dame el punto a "))      # intervalo
b = float(input("dame el punto b "))      # intervalo
tolera = float(input("dame la tolerancia "))  # tolerancia
iteramax = int(input("dame las iteraciones maximas "))  # itera máximo
muestras = 51  # gráfico
tramos = 50

# PROCEDIMIENTO
respuesta = puntofijo(gx,a,tolera)

# SALIDA
print(respuesta)
# GRAFICA
# calcula los puntos para fx y gx
xi = np.linspace(a,b,muestras)
fi = fx(xi)
gi = gx(xi)
yi = xi

import matplotlib.pyplot as plt

# Find the intersection between the functions f(x) and g(x)
idx = np.argwhere(np.diff(np.sign(fi - gi))).flatten()
if len(idx) > 0:
    x_inter = xi[idx[0]]
    y_inter = fx(x_inter)
    plt.plot(x_inter, y_inter, 'ro', label='Intersección')


plt.plot(xi,fi, label='f(x)')
plt.plot(xi,gi, label='g(x)')
plt.plot(xi,yi, label='y=x')

if (respuesta!= np.nan):
    plt.axvline(respuesta)
plt.axhline(0, color='k')
plt.title('Punto Fijo')
plt.legend()
plt.show()