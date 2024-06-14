# Q18. Write a python program that checks if two strings are anagrams of each other.

string1 = "Listen everyone"
string2 = "Silent everyone"

# Remove spaces and convert to lowercase
str1 = string1.replace(" ", "").lower()
str2 = string2.replace(" ", "").lower()

# Check if the sorted characters of both strings are equal
if sorted(str1) == sorted(str2):
    print(f'"{string1}" and "{string2}" are anagrams.')
else:
    print(f'"{string1}" and "{string2}" are not anagrams.')
