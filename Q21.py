# Q21. Write a python program that counts the occurrences of a specific element in a list.

elements = [1, 2, 3, 4, 2, 2, 5, 6, 2, 3]

# Element to count
element_to_count = 2

# Initializing the count to 0
count = 0

# Iterating through each element in the list and count occurrences of the specific element
for element in elements:
    if element == element_to_count:
        count += 1
print(f"The element {element_to_count} occurs {count} times in the list.")
