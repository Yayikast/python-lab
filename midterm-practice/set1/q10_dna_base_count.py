"""Validate a DNA string and count how often a given base occurs."""

dna = input("DNA: ")
base = input("base: ")
check = 0
count = 0

if dna == "" or len(base) != 1 or base not in "ATGC":
    print("This is not DNA String")
else:
    for char in dna:
        if char in "ATGC":
            pass
        else:
            check = check + 1
    if check == 0:
        for char in dna:
            if char == base:
                count = count + 1
            else:
                pass
        print("There are %d times that the base %s occur in this DNA." % (count, base))
    else:
        print("This is not DNA String")
