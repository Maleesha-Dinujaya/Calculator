# Define a function for addition
def add(a, b):
    return a + b

# Define a function for subtraction
def subtract(a, b):
    return a - b

# Define a function for multiplication
def multiply(a, b):
    return a * b

# Define a function for division with error handling
def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

# Define a function for exponentiation
def power(a, b):
    return a ** b

# Define a function for modulus (remainder)
def modulus(a, b):
    if b == 0:
        return "Error: Modulus by zero"
    return a % b

# Define a function for bitwise AND
def bitwise_and(a, b):
    return int(a) & int(b)

# Define a function for bitwise OR
def bitwise_or(a, b):
    return int(a) | int(b)

print("Welcome to My Calculator")

while True:
    try:
        # Input the first number
        a = float(input("Enter your first number: "))
        
        result = a  # Initialize the result with the first number
        
        while True:
            operation = input("Enter the operation (+, -, / (Division), *, ^ (Power), % (MOD), & (Bitwise And), | (Bitwise OR)), or 'done' to finish: ")
            
            if operation == 'done':
                break  # Exit the inner loop if 'done' is entered
            
            # Input the next number
            b = float(input("Enter the next number: "))
            
            if operation == '+':
                result = add(result, b)
            elif operation == '-':
                result = subtract(result, b)
            elif operation == '/':
                result = divide(result, b)
            elif operation == '*':
                result = multiply(result, b)
            elif operation == '^':
                result = power(result, b)
            elif operation == '%':
                result = modulus(result, b)
            elif operation == '&':
                result = bitwise_and(result, b)
            elif operation == '|':
                result = bitwise_or(result, b)
            else:
                print("Invalid operation. Please enter one of the specified operators.")
        
        print("Result:", result)

    except ValueError:
        print("Invalid input. Please enter valid numbers.")
    
    repeat = input("Do you want to perform another calculation? (yes/no): ")
    if repeat.lower() != "yes":
        break  # Exit the outer loop if the user does not want to repeat
