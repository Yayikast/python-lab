"""Open bank accounts and process withdrawals and deposits."""

bank = {}

def withdraw(num, val):
    if val <= bank[num]:
        bank[num] -= val
        print("Available amount of account number %d is %.2f." % (num, bank[num]))
    else:
        print("You don't have enough amount.")
        print("Available amount of account number %d is %.2f." % (num, bank[num]))

def deposit(num, val):
    bank[num] += val
    print("Available amount of account number %d is %.2f." % (num, bank[num]))

while True:
    x = input("Open bank account with initial amount (account number, amount): ").split()
    if len(x) == 2:
        acc, amt = x[0], x[1]
        acc, amt = int(acc), int(amt)
        bank[acc] = amt
    elif x == ["done"]:
        break

while True:
    x = input("Enter transaction (account number, withdraw/deposit, amount): ").split()
    if len(x) == 3:
        num, trn, val = x[0], x[1], x[2]
        num, val = int(num), int(val)
        
        if num in bank:
            if trn == "w":
                withdraw(num, val)
            elif trn == "d":
                deposit(num, val)
        else:
            print("Invalid account. Please enter transaction again.")
        
    elif x == ["done"]:
        break
