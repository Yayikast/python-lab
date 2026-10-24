"""Solve a 3x3 system of linear equations using the matrix inverse."""

import numpy as np

eq1 = []
eq2 = []
eq3 = []
sol = []

eq1.append(int(input("Input C1: ")))
eq1.append(int(input("Input C2: ")))
eq1.append(int(input("Input C3: ")))

sol.append(int(input("Input C4: ")))

eq2.append(int(input("Input C5: ")))
eq2.append(int(input("Input C6: ")))
eq2.append(int(input("Input C7: ")))

sol.append(int(input("Input C8: ")))

eq3.append(int(input("Input C9: ")))
eq3.append(int(input("Input C10: ")))
eq3.append(int(input("Input C11: ")))

sol.append(int(input("Input C12: ")))

eq = np.array([eq1, eq2, eq3])

print()
if not np.isclose(np.linalg.det(eq), 0):
    inv = np.linalg.inv(eq)
    ans = np.matmul(inv, sol)
    
    print("Solution:")
    print("x = %.2f" % ans[0])
    print("y = %.2f" % ans[1])
    print("z = %.2f" % ans[2])
else:
    print("Unable to find a solution")
