"""Read 3D points until END and print the distance of each segment and the total path."""

from math import sqrt
x = ""
point = {}
count = 1

def isnumber(a):
    try:
        float(a)
        return True
    except ValueError:
        return False

def dis(p1, p2):
    x1 = float(point[p1][0])
    y1 = float(point[p1][1])
    z1 = float(point[p1][2])
    x2 = float(point[p2][0])
    y2 = float(point[p2][1])
    z2 = float(point[p2][2])
    return sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)

while [y.upper() for y in x] != ["END"]:
    if count == 1:
        x = input("P1: ").split()
        
        check = True
        for i in x:
            if not isnumber(i):
                check = False
        
        if len(x) == 3 and check:
            point["P1"] = x
            count += 1
            
    else:
        fmt = "P" + str(count)
        x = input("%s: "%fmt).split()
        
        check = True
        for i in x:
            if not isnumber(i):
                check = False
                
        if len(x) == 3 and check:
            point[fmt] = x
            count += 1
            
if count >= 3:
    print("There are %d points in total." % (count-1))
    distotal = 0
    for i in range(1, count-1):
        d1 = ("P%s" % (i))
        d2 = ("P%s" % (i+1))
        print("P%s -> P%s = %.2f" % (i, i+1, dis(d1, d2)))
        distotal += dis(d1, d2)
    print("Total distance is %.2f units." % (distotal))
else:
    print("There are fewer than two points. There is no distance output.")
