"""For each digit in the input, print a row of * with every third mark replaced by #."""

seq = input("Input: ")

for char in seq:
    if char.isnumeric():
        char = int(char)
        for i in range(1, char+1):
            if i % 3 == 0:
                print("#", end="")
            else:
                print("*", end="")
        print()
    else:
        pass
