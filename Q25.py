# Q25. Write a program that copies the contents of one text file to another.

source_file_path = 'file1.txt'
destination_file_path = 'file2.txt'

# Open the source file and read its contents
with open(source_file_path, 'r') as source_file:
    contents = source_file.read()

# Open the destination file and write the contents to it
with open(destination_file_path, 'w') as destination_file:
    destination_file.write(contents)

print("File copied successfully.")
