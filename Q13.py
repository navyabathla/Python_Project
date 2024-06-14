# Q13. Write a program that asks the user for their birth year and calculates their age.

# Getting the current year
current_year = int(input("Enter the current year: "))

# Prompting the user to enter their birth year
while True:
    birth_year_str = input("Enter your birth year: ")
    if birth_year_str.isdigit():
        birth_year = int(birth_year_str)
        if birth_year <= current_year:
            break
        else:
            print("Invalid input: Please enter a birth year in the past or present.")
    else:
        print("Invalid input: Please enter a valid year (numeric).")

# Calculate the age
age = current_year - birth_year

# Print the calculated age
print("You are ",age, " years old.")
