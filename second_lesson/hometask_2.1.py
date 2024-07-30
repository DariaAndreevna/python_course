number = input("Please enter integer number:")
number = int(number)


first_numeral = number // 1000
print(first_numeral)

second_numeral = number % 1000 // 100
print(second_numeral)

third_numeral = number % 100 // 10
print(third_numeral)

fourth_numeral = number % 10
print(fourth_numeral)