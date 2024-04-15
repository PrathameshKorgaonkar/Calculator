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
        
        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            try:
                print("Result:", divide(num1, num2))
            except ValueError as e:
                print(e)
        else:
            print("Invalid input")
    except EOFError:
        print("\nInput was terminated unexpectedly. Please provide valid input.")
 
if __name__ == "__main__":
    main()
