# Life In Weeks

# Ask the current age to user
current_age = int(input("Enter your current age: "))

# Then calculate over 90

age = 90 - current_age


# Calculate days
days_remaining = age * 365

# Calculate Weeks
weeks_remaining = age *52

# Calculate Month
months_remaining = age *12

# Then print the combination of the values

print(f"You have the {days_remaining} days , {weeks_remaining} weeks and {months_remaining} months left .")
