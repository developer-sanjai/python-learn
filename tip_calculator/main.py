# Tip Calculator

# Prompt function
print("Welcome to tip calculator.")

# bill
bill= float(input("What was the total  bill? $ "))

#  percentage of tip
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))

# how many person do split the bill
people=int(input("How many person to split the bill? "))

# Calculate the tip and added the tip to the bill
tip_with_paid = tip / 100 * bill + bill

# Split the bill

bill_per_person = tip_with_paid / people
final_amount = round(bill_per_person, 2)

print(f"Each person should pay {final_amount}")