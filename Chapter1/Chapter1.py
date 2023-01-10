import numpy as np
#1.1
a = np.array([0,1,0,1])
b = np.array([0,1,1,0])
#building an and gate
#expected: 0,0,1,1
def AND(x, y):
    return (x * y)
#print(AND(a,b))
#1.2
def f(x):
    return ((5*(x*x)) - 4)
#f(x) = 5x^2 -4 
#f'(x) = 10x
def deriv(function, x, h = 0.000001):
    return round((function(x + h) - function(x))/h)
#print(int(deriv(f, 2))) #expected 20
def derivx5(function, x, h = 0.00000000001):
    bap = np.array([0,0,0,0,0,0,0,0,0,0])
    for i in range(0,10):
        bap[i] = deriv(function, x - 5 + i)
    return bap
#print(derivx5(f,2))
#1.3

