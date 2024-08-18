import string
import keyword
var = input("Enter any variable string:")
var = str(var)

if not var.islower() and var != "_":
    print(False)
elif len(var) > 1 and all([c == "_" for c in var ]):
    print(False)
elif var[0].isdigit():
    print(False)
elif any([c in string.punctuation and c != "_" for c in var]):
    print(False)
elif var in keyword.kwlist:
    print(False)
else:
    print(True)
