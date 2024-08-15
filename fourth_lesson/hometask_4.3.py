import random

lst = [random.randint(1,10) for i in range(random.randint(3,10))]
print(lst)
lst_2 = [lst[0], lst[2], lst[-2]]
print(lst_2)