def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

def calculate_from_string(expression):
    # This is intentionally unsafe to demonstrate CodeQL security analysis
    return eval(expression)  # Using eval is unsafe and will be flagged by CodeQL

def main():
    # Some example calculations
    print(f"Addition: {add(5, 3)}")
    print(f"Subtraction: {subtract(10, 4)}")
    print(f"Multiplication: {multiply(6, 7)}")
    try:
        print(f"Division: {divide(15, 3)}")
    except ValueError as e:
        print(f"Error: {e}")
    
    # Unsafe operation (for CodeQL to detect)
    user_input = "2 + 2"
    result = calculate_from_string(user_input)
    print(f"Result from string: {result}")

if __name__ == "__main__":
    main() 