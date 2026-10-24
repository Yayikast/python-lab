"""Draw a hollow rectangle with a border of random symbols."""

from random import choice
width = int(input("Rectangle width: "))
height = int(input("Rectangle height: "))
border = int(input("Border thickness: "))

for row in range(1, height+1):
    for col in range(1, width+1):
        if border+1 <= row <= height-border and border+1 <= col <= width-border:
            print(" ", end="")
        else:
            print(choice(["#","$","*"]), end="")        
    print()
