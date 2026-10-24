"""Volume of a right-corner tetrahedron from three edge lengths."""

while True:
    a = input("Input x,y,z :").split(",")
    if len(a) == 3:
        x, y, z = a[0], a[1], a[2]
        try:
            x, y, z = float(x), float(y), float(z)
            if x < 0 or y < 0 or z < 0:
                print("Invalid input.")
            else:
                print("Volume of Tetrahedron is %.2f cubic unit." % (x*y*z/6))
        except ValueError:
            print("Invalid input.")
    elif a == ["exit"] or a == ["Exit"]:
        print("Program ended.")
        break
    else:
        print("Enter 3 values.")
