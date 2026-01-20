import numpy as np

def add(n1, n2):
    return np.add(n1, n2)

def subtract(n1, n2):
    return np.subtract(n1, n2)

def multiply(n1, n2):
    return np.multiply(n1, n2) 

def divide(n1, n2):
    if n2 == 0:
        return "Cannot divide by zero"
    return np.divide(n1, n2)

print("Please select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
    # Get user input for operation
    choice = input("Enter choice (1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        try:
            # Get user input for numbers and convert to float
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            # Use numpy arrays for consistent input handling
            arr1 = np.array([num1])
            arr2 = np.array([num2])

            if choice == '1':
                result = add(arr1, arr2)[0]
                print(f"{num1} + {num2} = {result}")
            elif choice == '2':
                result = subtract(arr1, arr2)[0]
                print(f"{num1} - {num2} = {result}")
            elif choice == '3':
                result = multiply(arr1, arr2)[0]
                print(f"{num1} * {num2} = {result}")
            elif choice == '4':
                result = divide(arr1, arr2)
                if isinstance(result, str):
                    print(result)
                else:
                    print(f"{num1} / {num2} = {result[0]}")
            
            # Ask if the user wants to perform another calculation
            calc_again = input("Do you want to calculate again? (yes/no): ")
            if calc_again.lower() != 'yes':
                break

        except ValueError:
            print("Invalid input. Please enter numbers.")
    else:
        print("Invalid Input. Please enter a valid choice.")2