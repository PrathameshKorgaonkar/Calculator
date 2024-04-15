def add(x, y):
    return x + y
 
def subtract(x, y):
    return x - y
 
def multiply(x, y):
    return x * y
 
def main():
    print("Welcome to Calculator App!")
    
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    
    choice = input("Enter choice (1/2/3): ")
    
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    if choice == '1':
        print("Result:", add(num1, num2))
    elif choice == '2':
        print("Result:", subtract(num1, num2))
    elif choice == '3':
        print("Result:", multiply(num1, num2))
    else:
        print("Invalid input")
 
if __name__ == "__main__":
    main()
