# Q15. Write a program that reads data from a CSV file and prints it to the console.

# Path to the CSV file
file_path = 'data.csv'  # Replace with your CSV file path

# Read data from CSV file and print to console
with open(file_path, mode='r') as file:
    for line in file:
        print(line.strip())
