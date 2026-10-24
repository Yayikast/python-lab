"""Meal cost with a 10% service charge and 7% VAT."""

cost = float(input("Input the cost of a meal: "))
print("Service charge = %.2f" % (cost*0.1))
print("VAT = %.2f" % (cost*1.1*0.07))
print("Total cost = %.2f THB" % (cost*(1+0.1+(1.1*0.07))))
