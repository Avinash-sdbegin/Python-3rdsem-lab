# import re # importing the regular expression module , with  this module we will be  using search function
# password = input("Enter your password: ") # taking input from user
# password_len = len(password) # calculating length of password
# is_valid = False # initially setting is_valid to false,if it will satisfy all the conditions then it will be set to true,
#                  # we will check password length and first character


# # re.search() method searches a string for a specified value, and returns the position of the match
# # Check karo ki given pattern string ke andar kahin bhi match karta hai ya nahi.
# # If it finds a match, it returns a Match object, otherwise it returns None.


# while True: # infinite loop
#     if password_len < 7 or password_len > 20: # checking length of password
#         break # breaking the loop if condition is satisfied
#     elif not re.search("[a-z]", password): # checking for lowercase letter , atleast one lowercase letter should be present
#         break # breaking the loop if condition is satisfied
#     elif not re.search("[A-Z]", password): # checking for uppercase letter
#         break # breaking the loop if condition is satisfied
#     elif not re.search("[0-9]", password): # checking for digit
#         break # breaking the loop if condition is satisfied
#     elif not re.search("[$@#!]", password): # checking for special character
#         break # breaking the loop if condition is satisfied
#     elif re.search("\s", password): # checking for space
#         break # breaking the loop if condition is satisfied
#     else:
#         is_valid = True
#         break
    
# if is_valid:
#     print("The password is valid.")
# else:
#     print("The password is invalid, Re-enter the password and check Again.")


import re
while True:
    password = input("Enter your password: ")
    password_len = len(password)
    errors = [] # list to store error messages
    if password_len < 8 :
        errors.append("Minimum length should be 8 characters.")
    if not re.search("[a-z]", password):
        errors.append("At least one lowercase letter is required.")
    if not re.search("[A-Z]", password):
        errors.append("At least one uppercase letter is required.")
    if not re.search("[0-9]", password):
        errors.append("At least one digit is required.")
    if not re.search("[$@#!]", password):
        errors.append("At least one special character is required.")
    if re.search("\s", password):
        errors.append("Spaces are not allowed.")

    if errors:
        print("Password is invalid.")
        print("Please address the following issues:")
        print()
        for error in errors:
            print(error)
            print()
    else:
        print("Password is valid.")