"""Parse a name and age given in either order."""

x, y = input("Please enter your information: ").split(",")
if x.isalpha() and y.isnumeric():
    if 0 < int(y) < 120:
        name = x
        age = y
        print("Your name is %s." % x)
        print("Your age is %s." % y)
    else:
        print("Please enter your complete information.")
elif y.isalpha() and x.isnumeric():
    if 0 < int(x) < 120:
        name = y
        age = x
        print("Your name is %s." % y)
        print("Your age is %s." % x)
    else:
        print("Please enter your complete information.")
else:
    print("Please enter your complete information.")
