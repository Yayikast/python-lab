"""Rank players and award Gold to the top score and Silver to scores at or above the average."""

dct = {}
while True:
    x = input("Input: ").split()
    
    if x == ["done"]:
        break
    elif len(x) == 2:
        nam, scr = x[0], x[1]
        if scr.isnumeric():
            scr = int(scr)
            if nam in dct:
                print("Duplicated player")
            else:
                dct[nam] = scr
        else:
            print("Invalid input")

srtdct = dict(sorted(dct.items(), key=lambda item:item[1], reverse=True))

if len(srtdct) != 0:
    for i, j in srtdct.items():
        if j == max(srtdct.values()):
            print("%s\t%s\t%s" % (i, j, "Gold"))
        elif j >= (sum(srtdct.values())/len(srtdct)):
            print("%s\t%s\t%s" % (i, j, "Silver"))
        else:
            print("%s\t%s" % (i, j))
else:
    print("No players")
