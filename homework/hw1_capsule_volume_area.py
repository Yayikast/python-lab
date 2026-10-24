"""Volume and surface area of a capsule (cylinder with hemispherical ends)."""

from math import pi

r = float(input("Enter the radius of the capsule (in meters): "))
h = float(input("Enter the height of the middle cylinder (in meters): "))

v = ((4/3)*pi*r**3) + (pi*r*r*h)
a = (4*pi*r*r) + (2*pi*r*h)

print("The volume of the capsule is %.4f cubic meters" % v)
print("The surface area of the capsule is %.4f square meters" % a)
