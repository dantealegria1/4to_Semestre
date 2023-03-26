import scipy.optimize as opt
import numpy as np
fx = lambda x: np.exp(-x) - x
gx = lambda x: np.exp(-x)

def polola3():
    a = 0
    b = 1
    tolera = 1e-4
    iteramax = 100
    print(opt.fixed_point(gx,a,xtol=tolera,maxiter=iteramax))

