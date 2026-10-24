"""Area of a triangle, square, or circle from a single length."""

from math import pi
shape = input("Input a shape T/S/C: ")
d = input("Input a length: ")
if d.isnumeric():
    d = float(d)
    if d >= 0 and d == int(d):
        d = int(d)
        if shape == "T":
            print("The surface area of triangle is %.2f" % (d*d*0.25))
        elif shape == "S":
            print("The surface area of square is %.2f" % (d*d*0.5))
        elif shape == "C":
            print("The surface area of circle is %.2f" % (pi*d*d*0.25))
        else:
            print("Type must be only T/S/C.")
    else:
        print("Length must be more than or equal to zero.")
else:
    print("Length must be more than or equal to zero.")
