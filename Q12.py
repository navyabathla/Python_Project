# Q12. Write a python program that calculates the sum of the digits of a given number.

# Taking a number as input from the user
number = input("Enter a number: ")

# Initializing the sum to 0
sum_of_digits = 0

# Iterating over each character in the input number
for digit in number:
    # Convert the character to an integer and add it to the sum
    sum_of_digits += int(digit)

# Print the sum of the digits
print(f"The sum of the digits of the number is: {sum_of_digits}")
