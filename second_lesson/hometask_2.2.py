number = input("Please enter integer number:")
number = int(number)

first_numeral = number % 10
second_numeral = number % 100 // 10
third_numeral = number % 1000 // 100
fourth_numeral = number % 10000 // 1000
fifth_numeral = number // 10000

result = first_numeral * 10000 + second_numeral * 1000 + third_numeral * 100 + fourth_numeral * 10 + fifth_numeral
print(result)