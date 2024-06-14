# Q6. Write a program that reads the content of a text file and prints it to the console.

file_path = 'example.txt'

with open(file_path, 'r') as file:
    content = file.read()
    print(content)
