"""Group players by the sports they play."""

dct = {}

while True:
    z = input("who plays what?").split()
    
    if z == ["done"]:
        break
    else:
        name, sporttxt = z[0], z[1]
    
    sportlst = sporttxt.split(",")
    
    for sport in sportlst:
        if sport in dct:
            dct[sport].append(name)
        else:
            dct[sport] = [name]

for i, j in dct.items():
    print("%s is played by %s" % (i, j))
