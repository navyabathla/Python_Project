# Q11. Write a python program that generates the first n numbers in the Fibonacci sequence.

# Taking the value of n as input from the user
n = int(input("Enter the number of Fibonacci numbers to generate: "))

# Initialize the Fibonacci sequence
fibonacci_sequence = []

if n > 0:
    fibonacci_sequence.append(0)
if n > 1:
    fibonacci_sequence.append(1)

# Generate the Fibonacci sequence up to n numbers
for i in range(2, n):
    next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
    fibonacci_sequence.append(next_number)

# Print the Fibonacci sequence
print(f"The first {n} numbers in the Fibonacci sequence are: {fibonacci_sequence}")
