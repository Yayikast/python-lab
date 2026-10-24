"""Print every prime strictly between two positive integers."""

from math import sqrt, floor
start, end = input("Find all prime numbers between:").split()

if start.isnumeric() and end.isnumeric():
    start, end = int(start), int(end)
    if start > 0 and end > 0:
        for i in range(start + 1, end):
            check = 0
            for j in range(3, floor(sqrt(i))+1, 2):
                if i % j != 0:
                    pass
                else:
                    check = check + 1
                    continue
            if i == 2 or (i > 2 and check == 0 and i % 2 != 0):
                print(i)
            else:
                pass
    else:
        print("Invalid input")
else:
    print("Invalid input")
