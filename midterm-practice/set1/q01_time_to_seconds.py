"""Convert an HH:MM:SS time to total seconds with input validation."""

h, m, s = input("Input: ").split(":")

if h.isnumeric() and m.isnumeric() and s.isnumeric():
    h, m, s = float(h), float(m), float(s)
    if 0 <= h <= 23 and 0 <= m <= 59 and 0 <= s <= 59 and h == int(h) and m == int(m) and s == int(s):
        h, m, s = int(h), int(m), int(s)
        print("The number of seconds =", (h*60*60 + m*60 + s))
    else:
        print("Invalid time")
else:
    print("Invalid time")
