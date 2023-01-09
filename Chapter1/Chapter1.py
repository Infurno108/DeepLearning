import numpy as np

a = np.array([0,1,0,1])
b = np.array([0,1,1,0])
#building a XOR gate
#expected: 0,0,1,1

def xor(x: nparray, y: ndarray):
    return (x + y)

print(xor(a,b))
