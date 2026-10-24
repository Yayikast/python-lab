"""Convert a rectangular area in square feet to acres."""

length = float(input("Input length in ft: "))
width = float(input("Input width in ft: "))
print("The area in acres = %.2f" % ((length*width)/43560))
