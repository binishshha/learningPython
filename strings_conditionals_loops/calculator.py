while True:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))

    print("\nEnter your choice:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = int(input("Your choice: "))

    if choice == 1:
        print(f"The result is {a + b}")
    elif choice == 2:
        print(f"The result is {a - b}")
    elif choice == 3:
        print(f"The result is {a * b}")
    elif choice == 4:
        if b != 0:
            print(f"The result is {a / b}")
        else:
            print("Error: Division by zero")
    elif choice == 5:
        print("Exiting the calculator")
        break
    else:
        print("Invalid choice")

    if a < b:
        pass #does nothing if the condition is true
    else:
        print("Valid number comparison.\n")
