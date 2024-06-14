# Q9. Write a python program that checks if a substring is present in a given string.

# Take the main string as input from the user
main_string = input("Enter the main string: ")

# Take the substring as input from the user
substring = input("Enter the substring to search for: ")

# Checking if the substring is present in the main string using 'in' operator
if substring in main_string:
    print(f"The substring '{substring}' is present in the main string.")
else:
    print(f"The substring '{substring}' is not present in the main string.")
