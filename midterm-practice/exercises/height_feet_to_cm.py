"""Convert a height in feet and inches to centimetres."""

feet = float(input("Input the number of feet: "))
inch = float(input("Input the number of inches: "))
print("The height in cm = %.2f" % ((feet*12 + inch)*2.54))
