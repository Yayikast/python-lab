"""Check whether three side lengths can form a triangle."""

a = input("Input: a=? ")
b = input("Input: b=? ")
c = input("Input: c=? ")

if a.isnumeric() and b.isnumeric() and c.isnumeric():
    a, b, c = float(a), float(b), float(c)
    if a > 0 and b > 0 and c > 0:
        x = max(a, b, c)
        if x < a + b + c - x:
            print("Output: Form a triangle")
        else:
            print("Output: Can't form a triangle")
    else:
        print("Some input is not a number")
else:
    print("Some input is not a number")
