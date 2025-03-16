# Your Student ID: 230543606
# Your Name and Surname: Saed Abdul Rahim
# ex10.py
while True:
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operation = input("Choose operation (+, -, *, /): ")
        if operation == "+":
            print("Result:", num1 + num2)
        elif operation == "-":
            print("Result:", num1 - num2)
        elif operation == "*":
            print("Result:", num1 * num2)
        elif operation == "/":
            if num2 == 0:
                print("Error: Division by zero")
            else:
                print("Result:", num1 / num2)
        else:
            print("Invalid operation")
    except ValueError:
        print("Invalid input")
    cont = input("Perform another calculation? (yes/no): ").strip().lower()
    if cont != "yes":
        break
