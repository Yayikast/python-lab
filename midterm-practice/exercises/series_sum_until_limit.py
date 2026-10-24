"""Add terms of the series sqrt(2)*i - 1 until the sum reaches v."""

from math import sqrt
v = input("Input v: ")
total = 0
count = 0

try:
    v = float(v)
    while total < v:
        count = count + 1
        total = total + sqrt(2)*(count)-1
    print("Output: n = %d, S = %.2f" % (count, total))
except ValueError:
    print("Invalid input")
