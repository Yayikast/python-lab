"""Find the longest distance between three points in 3D space."""

import numpy as np
from math import sqrt

def dis(x1, x2):
    dif = x1 - x2
    sqr = dif**2
    return sqrt(sqr[0]+sqr[1]+sqr[2])

P1 = np.array(input("Input coordinate of P1: ").split()).astype('float64')
P2 = np.array(input("Input coordinate of P2: ").split()).astype('float64')
P3 = np.array(input("Input coordinate of P3: ").split()).astype('float64')

dismax = max(dis(P1,P2), dis(P2,P3), dis(P3,P1))
print("Output:")
print("The longest distance = %.2f" % dismax)
