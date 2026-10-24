"""Travel time from speed and distance, shown as decimal hours or hours and minutes."""

v = input("Enter speed in mph: ")
if v.isnumeric() :
    v = float(v)
    if v == int(v) and v > 0:
        v = int(v)
        d = input("Enter distance in miles: ")
        if d.isnumeric() :
            d = float(d)
            if d == int(d) and d > 0:
                d = int(d)
                dis = input("Enter output format (D or M): ")
                if dis == "D":
                    print("At %d mph, it will take" % v)
                    print("%.2f hours to travel %d miles." % (d/v, d))
                elif dis == "M":
                    time = d/v
                    hour = time // 1
                    min = (time % 1)*60
                    print("At %d mph, it will take" % v)
                    print("%d hours and %d minutes to travel %d miles." % (hour, min, d))
                else:
                    print("Invalid input")
            else:
                print("Invalid input")
        else:
            print("Invalid input")
    else:
        print("Invalid input")
else:
    print("Invalid input")
