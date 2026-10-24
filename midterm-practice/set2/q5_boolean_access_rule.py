"""Evaluate an access rule, a or not (b or c), from three boolean inputs."""

a, b, c = input("a, b, c = ").split()
count = 0

if a == "True":
    a = True
    count = count + 1
elif a == "False":
    a = False
    count = count + 1
if b == "True":
    b = True
    count = count + 1
elif b == "False":
    b = False
    count = count + 1
if c == "True":
    c = True
    count = count + 1
elif c == "False":
    c = False
    count = count + 1
    
if count == 3:
    status = ((a) or (not(b or c)))
    if status == True:
        print("Grant")
    else:
        print("Deny")
else:
    print("Invalid input")
