# Program to check if a person is a minor, adult, or senior based on age input
# Assuming the maximum age of a person is 100 years

age = int(input("Enter your age: "))
if age > 0 and age < 18:
    print("The person is a minor.")
elif age >= 18 and age <= 65:
    print("You are an adult.")
elif age > 65 and age <= 100:
    print("You are a senior.")
else:
    print("Invalid age. Please enter a valid age between 0 and 100.")
