"""Print a right-aligned number pyramid for 1-9."""

while True:
    x = int(input("Enter an integer number (0 to exit): "))
    if x == 0:
        print("Exit program. Bye!")
        break
    elif 1 <= x <= 9:
        for j in range(x-1, -1, -1):
            print(" "*j + (str(x)+" ")*(x-j))
        print()
    else:
        print("Valid value is between 0 and 9!")
        break
