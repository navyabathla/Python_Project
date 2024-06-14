# Q23. Write a program that converts temperature from Celsius to Fahrenheit and vice versa based on
# user input.

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Getting user input for the conversion direction
conversion_direction = input("Type 'C' to convert from Celsius to Fahrenheit or 'F' to convert from Fahrenheit to Celsius: ").strip().upper()

# Performing the conversion based on user input
if conversion_direction == 'C':
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius}°C is equal to {fahrenheit}°F")
elif conversion_direction == 'F':
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit}°F is equal to {celsius}°C")
else:
    print("Invalid input. Please type 'C' or 'F'.")
