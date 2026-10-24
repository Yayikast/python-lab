"""Print every lowercase letter between two given letters."""

seq = "abcdefghijklmnopqrstuvwxyz"
x1 = input("Give me a character: ")
x2 = input("Give me another character: ")
start = min(x1, x2)
end = max(x1, x2)
print("Output:")
if start in seq and end in seq:
    for char in seq:
        if start <= char <= end:
            print(char, end="")
        else:
            pass
    print()
else:
    print("You need to input two characters.")
