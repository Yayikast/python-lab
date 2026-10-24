"""Earn reward points on purchases and redeem them."""

from math import floor
pts = 100

while True:
    typ, amt = input("Command: ").split()
    amt = int(amt)
    if typ == "done" and amt == 0:
        break
    elif typ == "P":
        p = floor(amt/50)
        pts += p
        print("You earned %d points" % p)
        print("Your accumulated points = %d points" % pts)
    elif typ == "R":
        if pts >= amt:
            pts -= amt
            print("You redeemed %d points" % amt)
            print("Your accumulated points = %d points" % pts)
        else:
            print("Not enough points")
    else:
        print("Invalid command")
