"""Record scores by 4-digit student ID with validation, then list them with the average."""

dct = {}

def avg(x):
    s = 0
    for i in x:
        s += i
    return s/len(x) 

while True:
    stid, scr = input("Enter student ID and score: ").split()
    if stid == "done" and scr == "0":
        break
    elif stid.isnumeric() and scr.isnumeric():
        if len(stid) == 4:
            stid, scr = int(stid), int(scr)
            if 0 <= scr <= 100:
                if stid in dct:
                    print("The ID is already recorded!")
                else:
                    dct[stid] = scr
            else:
                print("Invalid score!")
        else:
            print("Invalid ID format!")
    elif not stid.isnumeric():
        print("Invalid ID format!")
    else:
        print("Invalid score!")

print("List:")
if len(dct) == 0:
    print("> no score is recorded!")
else:
    srtdct = dict(sorted(dct.items(), key=lambda item:item[0]))
    for i, j in srtdct.items():
        print("%s\t%s" % (i, j))
    print("There are %d student(s). The average score is %.2f points." % (len(srtdct), avg(srtdct.values())))
