"""Draw a symmetric pattern of alternating * and 0 characters."""

x = input("Input: ")
if x.isnumeric():
    x = float(x)
    if x == int(x) and x >= 3:
        x = int(x)
        for row in range(1, 2*x):
            for col in range(1, 2*x+1):
                if row +1 <= col <= 2*x - row:
                    print(" ", end="")
                elif row > x and 2*x - row + 1 <= col <= row:
                    print(" ", end="")
                else:
                    if col <= x:
                        if abs(x - col) % 2 == 0:
                            print("*", end="")
                        else:
                            print("0", end="")
                    else:
                        if abs(x - col) % 2 == 1:
                            print("*", end="")
                        else:
                            print("0", end="")
            print()
    else:
        print("Your input is invalid.")
else:
    print("Your input is invalid.")
