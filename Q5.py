# Q5. Write a program that takes a string input from the user and writes it to a text file.

# Taking input from the user
user_input = input("Enter a string: ")

# Opening a text file in write mode
with open("output.txt", "w") as file:
    # Writing the user input to the file
    file.write(user_input)

print("String written to file successfully!")
