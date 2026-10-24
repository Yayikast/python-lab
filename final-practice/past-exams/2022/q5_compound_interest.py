"""Five-year compound interest table."""

while True:
    z = input("Input initial money and interest rate: ").split()
    
    if len(z) == 2:
        n, rate = z[0], z[1]
        try:
            n, rate = float(n), float(rate)
            for i in range(1, 6):
                inter = rate/100*n
                print("YEAR %d --- %.2f + %.2f = %.2f" % (i, n, inter, n+inter))
                n += inter
            print("*****")
        
        except ValueError:
            print("Invalid input, please try again.")
        
    elif z == ["exit"]:
        break
    
    else:
        print("Invalid input, please try again.")
