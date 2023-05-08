import Addition
import Subtraction

print("Operations Available.")
print("1. Addition")
print("2. Subtraction")

while True:
    # take input from the user
    choice = input("\nEnter choice:\n1 - Addition\n2 - Subtraction")

    # check if choice is one of the two options
    if choice in ('1', '2'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", Addition.Add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", Subtraction.Subtract(num1, num2))
 
        
    # check if user wants another calculation
    # break the while loop if answer is no
    next_calculation = input("Let's do next calculation? (yes/no): ")
    if next_calculation == "no":
        break
    
    else:
        print("Invalid Input")

