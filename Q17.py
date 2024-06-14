# Q17. Write a program in python that converts a given string to title case (first letter of each word
# capitalized).

input_string = "hello all, my name is navya bathla"

# Spliting the input string by spaces
words = input_string.split(' ')

# Capitalizing the first letter of each word
title_case_words = [word.capitalize() for word in words]

# Joining the words back together with spaces
title_case_string = ' '.join(title_case_words)

# Printing the results
print("Original:", input_string)
print("Title Case:", title_case_string)
