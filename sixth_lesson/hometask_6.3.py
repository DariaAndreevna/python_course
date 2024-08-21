number = int(input("Please enter integer number:"))

result = number
while result >= 9:
    digits = [int(digit) for digit in str(result)]
    result = 1
    for digit in digits:
        result = result * digit

print(result)
