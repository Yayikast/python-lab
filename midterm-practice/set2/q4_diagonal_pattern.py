"""Draw a main or anti-diagonal pattern with a chosen symbol."""

sym = input("Enter a special character: ")
size = input("Enter the size of the pattern: ")
option = input("Enter option for the pattern: ")

if sym in "#$@*^":
    if size.isnumeric():
        size = float(size)
        if size == int(size) and size >= 1:
            size = int(size)
            if option.isnumeric():
                option = float(option)
                if option == int(option) and option >= 1:
                    option = int(option)
                    if option == 1:
                        for row in range(size):
                            for col in range(size):
                                if row == col:
                                    print("%s" % sym, end="")
                                else:
                                    print(".", end="")
                            print()
                    elif option == 2:
                        for row in range(size):
                            for col in range(size):
                                if row + col == size - 1:
                                    print("%s" % sym, end="")
                                else:
                                    print(".", end="")
                            print()
                    else:
                        print("Wrong input values.")
                else:
                    print("Wrong input values.")
            else:
                print("Wrong input values.")
        else:
            print("Wrong input values.")
    else:
        print("Wrong input values.")
else:
    print("Wrong input values.")
