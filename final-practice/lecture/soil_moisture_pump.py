"""Simulate a water pump that raises soil moisture to 70%."""

x = input("Input: ")

try:
    x = int(x)
    if 0 <= x <= 100:
        while x < 70:
            x += 5
            print("Watering... Current soil moisture: %s" % x + "%")
        print("Soil moisture is sufficient. Stopping the water pump.")
    else:
        print("Invalid soil moisture level.")

except ValueError:
    print("Invalid input. Please input an integer")
