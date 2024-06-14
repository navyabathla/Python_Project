# Q16. Write a program in python that counts the frequency of each character in a string.

# Taking a string as input from the user
input_string = input("Enter a string: ")

# Initializing an empty dictionary to store character frequencies
char_frequency = {}

# Count frequency of each character in the string
for char in input_string:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

# Print the character frequencies
print("Character frequencies:", char_frequency)

