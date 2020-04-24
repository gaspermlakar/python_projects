first_number = int(input("First number: "))
operation = input("Enter OPERATION ( +, -, *, /, 2) ")
second_number = int(input("Second number "))

if operation == "+":
    print(first_number + second_number)
elif operation == "-":
    print(first_number - second_number)
elif operation == "*":
    print(first_number * second_number)
elif operation == "/":
    print(first_number / second_number)
else:
    print("Wrong math operation.")
