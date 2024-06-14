# Q14. Write a program that reads multiple lines of input from the user until they enter an empty line,
# then prints all the lines.

# Initializing an empty list to store lines of input
lines = []

# Reading input lines until an empty line is entered
print("Enter lines (empty line to stop):")
while True:
    line = input()
    if line == "":
        break
    lines.append(line)

# Print all the lines entered
print("\nLines entered:")
for line in lines:
    print(line)
