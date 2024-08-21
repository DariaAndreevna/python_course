import string

letters_range = str(input("Please enter the range of letters in the following format x-y:"))
first_letter = letters_range[0]
first_index = string.ascii_letters.find(first_letter)
second_letter = letters_range[-1]
second_index = string.ascii_letters.find(second_letter)

print(string.ascii_letters[first_index:second_index + 1])
