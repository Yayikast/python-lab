"""Check each number for primality and sum the primes."""

from math import sqrt, floor

lst = []
def prm(x):
    check = True
    if x != 2 and x%2 == 0:
        check = False
    elif x > 1:
        for i in range(3, x, 2):
            if x%i == 0:
                check = False
    else:
        check = False
    return check

while True:
    x = input("Enter a number ")
    if x == "done":
        break
    else:
        x = int(x)
        if prm(x):
            print("It is a prime")
            lst.append(x)
        else:
            print("It is not a prime")
print("The sum of all primes is ", sum(lst))
