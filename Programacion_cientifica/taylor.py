import math
import sympy

def taylor_math(f, a, n):
    def nth_derivative(f, n):
        if n == 0:
            return f
        else:
            return nth_derivative(math.deriv(f), n-1)

    result = 0
    for i in range(n+1):
        result += (nth_derivative(f, i) / math.factorial(i)) * (x - a)**i
    return result

def taylor_sympy(f, a, n):
    x = sympy.symbols('x')
    return f.series(x, x0=a, n=n+1).removeO()

x = 0
n = 5
print(taylor_math(math.sin, x, n)) # Imprime: x - x**3/6 + x**5/120
print(taylor_sympy(sympy.sin(x), x, n)) # Imprime: x - x**3/6 + x**5/120
