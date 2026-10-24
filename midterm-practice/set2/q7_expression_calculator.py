"""Parse a*b*c and compute one of two expressions."""

from math import sqrt
a, b, c = input("Please enter an input: ").split("*")
choice = input("Please enter your choice (1 or 2): ")

if a.isnumeric() and b.isnumeric() and c.isnumeric():
    a, b, c = float(a), float(b), float(c)
    if a == int(a) and b == int(b) and c == int(c) and a > 0 and b > 0 and c > 0:
        a, b, c = int(a), int(b), int(c)
        if choice == "1":
            print("The output is %.2f" % (a + sqrt(b*b + c**3)))
        elif choice == "2":
            d = int(str(a)+str(b))
            print("The output is %.2f" % (d % c))
        else:
            print("Invalid Inputs")
    else:
        print("Invalid Inputs")
else:
    print("Invalid Inputs")
