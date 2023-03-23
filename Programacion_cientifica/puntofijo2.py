import scipy.optimize as opt
import numpy as np
fx = lambda x: np.exp(-x) - x
gx = lambda x: np.exp(-x)

a = float(input("dame el punto a "))      # intervalo
b = float(input("dame el punto b "))      # intervalo
tolera = float(input("dame la tolerancia "))  # tolerancia
iteramax = int(input("dame las iteraciones maximas "))  # itera máximo

print(opt.fixed_point(gx,a,xtol=tolera,maxiter=iteramax))

import matplotlib.pyplot as plt

x = np.linspace(a, b, 1000)
yfx = fx(x)
ygx = gx(x)

plt.plot(x, yfx, label='f(x)')
plt.axhline(y=0, color='black', linestyle='--')
plt.legend()
plt.show()
