"""Process deposits and withdrawals against a balance until 'done 0'."""

x = int(input("Enter the initial balance: "))
while True:
    typ, amt = input("Transaction type and amount (\"done 0\" to exit): ").split()
    
    if typ == "done" and amt == "0":
        break
    else:
        amt = int(amt)
        if amt >= 0:
            if typ == "D":
                x += amt
                print("> Deposit = %d THB, current balance = %d THB." % (amt, x))
            elif typ == "W":
                if x >= amt:
                    x -= amt
                    print("> Withdrawal = %d THB, current balance = %d THB." % (amt, x))
                else:
                    print("> Invalid transaction!")
            else:
                print("> Invalid transaction!")
        else:
            print("> Invalid transaction!")
print("> Current balance = %d THB." % x)
