# Define addition, substraction,multiplication and division function
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Division by zero is not possible."

# Define the calculator function that interacts with the user
def calculator():
    print("This is a Simple Calculator")
    
    while True:
        print("\nSelect operation.")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")  # Add an option to exit the calculator
        
        option = input("Enter the operation you want to perform (1/2/3/4/5): ")

        if option in ('1', '2', '3', '4'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if option == '1':
                print(num1, "+", num2, "=", add(num1, num2))
            elif option == '2':
                print(num1, "-", num2, "=", subtract(num1, num2))
            elif option == '3':
                print(num1, "*", num2, "=", multiply(num1, num2))
            elif option == '4':
                print(num1, "/", num2, "=", divide(num1, num2))
        elif option == '5':
            print("Exiting the calculator. Goodbye!")
            break  # exits the loop
        else:
            print("Invalid option. Please choose a valid operation (1/2/3/4/5)")
1
# Call calculator function
calculator()