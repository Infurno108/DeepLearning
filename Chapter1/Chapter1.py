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

def deriv(function, x, h = 0.000001):
    return ((function(x + h) - function(x))/h)

#print(int(deriv(f, 2))) #expected 20

def derivx5(function, x, h = 0.000001):
    array = np.array(10)
    for i in range(0, 10):
        np.append(array, deriv(function, x + i - 5))  
    return array
print(derivx5(f,2))
