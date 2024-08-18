reload = "yes"

while reload == "yes":

    print("You have following operations: +, - , * , /")
    first_number = int(input("Please enter first integer number:"))
    second_number = int(input("Please enter second integer number:"))
    operation = str(input("Please enter chosen operation:"))

    if operation == "+":
        result = first_number + second_number
    elif operation == "-":
        result = first_number - second_number
    elif operation == "*":
        result = first_number * second_number
    elif operation == "/" and second_number != 0:
        result = first_number / second_number
    elif operation == "/" and second_number == 0:
        result = "Invalid operation. You can not divide by zero."
    else:
        result = "Invalid operation. Please use following operations: +, -, *, /"
    print(result)
    reload = str(input("Do you want to continue?"))
    reload = reload.strip()

