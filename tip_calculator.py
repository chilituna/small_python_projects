#to calculate tip and share the bill

print("Welcome to the tip calculator.")
total = float(input("Please enter the total bill (EUR). Use dot as separator if needed.\n"))
tip = float(input("How much tip would you like to give? (%)\n"))
people = float(input("How many people are sharing the bill?\n"))
pay = total * (tip / 100 + 1) / people
print("Each person should pay %.2f EUR." % pay)
