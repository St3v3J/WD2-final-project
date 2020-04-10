x = int(input("Enter the value for x: "))

y = int(input("Enter the value for y: "))

operation = input("Choose math operator (+, -, *, /: ")

if operation == "+":
    print(x + y)
elif operation == "-":
    print(x - y)
elif operation == "*":
    print(x * y)
elif operation =="/":
    print(x / y)
else:
    print("Negative you did not provide the correct math operator.")

