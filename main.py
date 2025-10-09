from math_utils import add, subtract, multiply, divide

def get_number(prompt):
    """Prompt user for a number with input validation."""
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("❌ Invalid input! Please enter a number.")

def main():
    print("=== Simple Calculator ===")
    
    num1 = get_number("Enter first number: ")
    num2 = get_number("Enter second number: ")

    try:
        print(f"Addition: {add(num1, num2)}")
        print(f"Subtraction: {subtract(num1, num2)}")
        print(f"Multiplication: {multiply(num1, num2)}")
        print(f"Division: {divide(num1, num2)}")
    except ZeroDivisionError:
        print("⚠️  Error: Cannot divide by zero!")

if __name__ == "__main__":
    main()

