"""Print rows of digits that rotate left on odd rows and count down on even rows."""

w, h = input("Input: ").split()
if w.isnumeric() and h.isnumeric():
    w, h = float(w), float(h)
    if w == int(w) and h == int(h) and 1 <= w <=9 and 1 <= h <= 9:
        w, h = int(w), int(h)
        odd = 1
        even = w
        for row in range(1, h+1):
            if row % 2 == 1:
                for i in range(odd, w+1):
                    print(i, end="")
                for i in range(1, odd):
                    print(i, end="")
                odd = odd + 1
                print()
            else:
                for i in range(even, 0, -1):
                    print(i, end="")
                for i in range(w, even, -1):
                    print(i, end="")
                even = even - 1
                print()
    else:
        print("Invalid input")
else:
    print("Invalid input")
