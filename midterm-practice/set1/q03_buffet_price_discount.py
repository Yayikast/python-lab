"""Buffet price by group size with discount codes."""

num = int(input("Input (Number of customers): "))
code = input("Input (Discount code): ")

if 1 <= num <= 3:
    print("%d person x 399.00 baht" % num)
    price = num*399
    print("A subtotal price is %.2f baht" % price)
elif 4 <= num <= 6:
    print("%d person x 499.00 baht" % num)
    price = num*499
    print("A subtotal price is %.2f baht" % price)
else:
    print("%d person x 599.00 baht" % num)
    price = num*599
    print("A subtotal price is %.2f baht" % price)
    
if code == "CASH":
    dis = 5
    print("On-top discount 5%")
elif code == "BIRTHDAY":
    dis = 10
    print("On-top discount 10%")
elif code == "COVID":
    dis = 30
    print("On-top discount 30%")
else:
    dis = 0
    print("On-top discount 0%")

print("A total price is %.2f baht" % (price*(100-dis)/100))
