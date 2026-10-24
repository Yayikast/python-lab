"""Compute the EAN-13 barcode check digit for a 12-digit string."""

seq = input("Input 12-digit string: ")
check = 0
s = 0
if len(seq) == 12 and seq.isnumeric():
    #seq = int(seq)
    for char in seq:
        if check % 2 == 0:
            s = s + int(char)
        else:
            s = s + (int(char)*3)
        check = check + 1
    t = 10 - (s % 10)
    if t == 10:
        c = 0
    else:
        c = t
    print("Output: check digit =", c)
else:
    print("Invalid input")
