print("You have following operations: 1 - +, 2 - -, 3 - *, 4 - /")
first_number = int(input("Please enter first integer number:"))
second_number = int(input("Please enter second integer number:"))
operation = int(input("Please enter chosen operation:"))

if operation == 1:
    result = first_number + second_number
elif operation == 2:
    result = first_number - second_number
elif operation == 3:
    result = first_number * second_number
elif operation == 4 and second_number != 0:
    result = first_number / second_number
elif operation == 4 and second_number == 0:
    result = "Invalid operation. You can not divide by zero."
else:
    result = "Invalid operation. Please use following operations: 1 - +, 2 - -, 3 - *, 4 - /"

print(result)