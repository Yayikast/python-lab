"""Cylinder volume calculator with input validation."""

from math import pi

while True:
    z = input("Input radius and height: ").split()
    if len(z) == 2:
        r, h = z[0], z[1]
        
        try:
            r = float(r)
            h = float(h)
            if 0 > r or 0 > h:
                print("Invalid inputs")
            else:
                print("The cylinder volume is %.2f" % (pi*r*r*h))
        except ValueError:
            print("Invalid inputs")
  
    elif z == ["done"]:
        break
    else:
        print("Invalid inputs")
