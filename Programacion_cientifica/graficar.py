import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# Definir la función
def f(x):
    return x**2 - 4

# Crear un array de valores x
x = np.linspace(-5, 5, 100)

# Evaluar la función en los valores x
y = f(x)

# Encontrar la raíz de la función
root = fsolve(f, 0)

# Graficar la función y la raíz
plt.plot(x, y)
plt.axhline(y=0, color='k')
plt.axvline(x=root, color='r')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
