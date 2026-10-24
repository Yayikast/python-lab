"""Read numbers until their sum exceeds 1000, then print them sorted with the total."""

lst = []
check = True
while sum(lst) <= 1000:
    x = input("Numbers: ")
    
    if x == "EXIT":
        print("Exit without summary.")
        check = False
        break
    
    try:
        x = float(x)
        lst.append(x)
        
    except ValueError:
        pass

if check:
    print("----------")
    arranged = sorted(lst)
    print(", ".join("%.2f" % i for i in arranged))
    print("sum = %.2f" % sum(lst))
