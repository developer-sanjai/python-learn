#   BMI Calculator


# Ask the height 
height = input("Enter you height in m: ")

height_as_float = float(height)

# Ask the weight
weight = input("Enter your weight in kg:")

weight_as_int = int(weight)
# Then calculate the BMI

bmi = weight_as_int / height_as_float ** 2

bmi_as_int = int(bmi)

# Print the BMI result

print(bmi_as_int)