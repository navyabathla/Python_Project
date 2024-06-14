# Q19. Write a python program that removes all punctuation from a given string.

# Example string with punctuation
input_string = "Hello, world! This is a test string with punctuation: @#$%^&*(){}[]"

# Define punctuation characters
punctuation_chars = '''!()-[]{};:'",<>./?@#$%^&*_~'''

# Remove punctuation
cleaned_string = ""
for char in input_string:
    if char not in punctuation_chars:
        cleaned_string += char

# Print original and cleaned strings
print("Original string:", input_string)
print("String without punctuation:", cleaned_string)
