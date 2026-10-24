"""Collect unique student scores and print them ranked from highest to lowest."""

lst = {}

while True:
    x = input("Enter student name and score: ").split()
    
    if x == ["end"]:
        break
    
    elif len(x) == 2:
        nam, scr = x[0], x[1]
        scr = int(scr)
        
        if nam in lst:
            print("Duplicate name!")
        elif nam == "end" and scr == 0:
            break
        elif 0 <= scr <= 100:
            lst[nam] = scr
        else:
            print("Invalid score!")
    
srtlst = dict(sorted(lst.items(), key=lambda item:item[1], reverse=True))

print("List:")
for a, b in srtlst.items():
    print("%s\t%d" % (a, b))
