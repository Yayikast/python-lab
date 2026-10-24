"""Sum every integer between two numbers and print the square root of the sum."""

from math import sqrt
a, b = input("Please enter two integers: ").split(" ")

if a.isnumeric() and b.isnumeric():
    a, b = float(a), float(b)
    if a == int(a) and b == int(b) and 1 <= a <= 30 and 1 <= b <= 30:
        a, b = int(a), int(b)
        if a <= b:
            min = a
            max = b
        else:
            min = b
            max = a
        print("The minimum number is", min)
        print("The maximum number is", max)
        sum = 0
        for i in range(min, max+1):
            sum = sum + i
        print("The square root of the summation is %.2f" % sqrt(sum))
    else:
        print("Invalid Inputs")
else:
    print("Invalid Inputs")
