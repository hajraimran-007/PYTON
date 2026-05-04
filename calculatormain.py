# simple_calculator.py

import calculator

while True:
    print("\n--- Simple Calculator ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulus")
    print("0. Exit")

    choice = input("Enter choice (0-5): ")

    if choice == '0':
        print("Goodbye!")
        break

    if choice not in ['1', '2', '3', '4', '5']:
        print("Invalid choice!")
        continue

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice == '1':
        print("Result:", calculator.add(a, b))

    elif choice == '2':
        print("Result:", calculator.subtract(a, b))

    elif choice == '3':
        print("Result:", calculator.multiply(a, b))

    elif choice == '4':
        print("Result:", calculator.divide(a, b))

    elif choice == '5':
        print("Result:", calculator.modulus(a, b))

    again = input("Continue? (y/n): ")

    if again != 'y':
        print("Goodbye!")
        break