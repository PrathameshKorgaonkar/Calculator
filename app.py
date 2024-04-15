def add_numbers(num1, num2):
    return num1 + num2
 
def subtract_numbers(num1, num2):
    return num1 - num2
 
def multiply_numbers(num1, num2):
    return num1 * num2
 
def divide_numbers(num1, num2):
    if num2 == 0:
        raise ValueError("Cannot divide by zero")
    return num1 / num2
 
def perform_operation(num1, num2, choice):
    if choice == '1':
        return add_numbers(num1, num2)
    elif choice == '2':
        return subtract_numbers(num1, num2)
    elif choice == '3':
        return multiply_numbers(num1, num2)
    elif choice == '4':
        return divide_numbers(num1, num2)
    else:
        raise ValueError("Invalid choice")
 
def main():
    try:
        print("Welcome to Calculator App!")
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        print("Select operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        
        choice = input("Enter choice (1/2/3/4): ")
        
        result = perform_operation(num1, num2, choice)
        print("Result:", result)
        
    except ValueError as e:
        print("Error:", e)
    except EOFError:
        print("\nInput was terminated unexpectedly. Please provide valid input.")
 
if __name__ == "__main__":
    main()
