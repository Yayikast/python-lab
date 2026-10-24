"""Count students per engineering section and list them by grade."""

dct = {'ce':0, 'che':0, 'ec':0, 'ie':0, 'me':0}
dis = {}

while True:
    x = input("Input: ").split()
    
    if x == ["done"]:
        break
    elif len(x) == 3:
        nam, sec, grd = x[0], x[1], float(x[2])
        
        if 0 <= grd <= 4:
            if sec in dct:
                lst = [sec, grd]
                dis[nam] = lst
                
                dct[sec] += 1
                
            else:
                print("ERROR")
        else:
            print("ERROR")

srtdis = dict(sorted(dis.items(), key=lambda item:item[1][1], reverse=True))

print("----SUMMARY----")
for i, j in dct.items():
    print("%s = %d" % (i, j))

print("----LIST----")
for i, j in srtdis.items():
    print("%s %s %.2f" % (i, j[0], j[1]))
