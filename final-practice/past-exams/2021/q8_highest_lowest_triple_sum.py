"""Print the largest and smallest sums of three integers from the input."""

lst = []

while True:
    x = input("Input: ")
    if x == "done":
        break
    else:
        try:
            x = float(x)
            if x == int(x):
                x = int(x)
                lst.append(x)
            else:
                print("Invalid input")
        except ValueError:
            print("Invalid input")

lst.sort()
if len(lst) >= 3:
    mins = lst[0]+lst[1]+lst[2]
    maxs = lst[-1]+lst[-2]+lst[-3]
    print("The highest sum and the smallest sum are %d and %d." % (maxs, mins))
else:
    print("Not enough inputs")
