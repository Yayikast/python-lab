"""Read an n x n matrix and print its determinant and inverse with NumPy."""

import numpy as np
n = int(input("Input size of matrix: "))

mat = []

for row in range(1, n+1):
    matrow = []
    for col in range(1, n+1):
        x = int(input("Input element at row %s column %s: " % (row, col)))
        matrow.append(x)
    mat.append(matrow)

print()
print("Output:")

matarray = np.array(mat)
print("Matrix =")
print(matarray)

det = np.linalg.det(matarray)
print("Determinant =", det)

if not np.isclose(det, 0):
    print("Inverse matrix =")
    print(np.linalg.inv(matarray))
