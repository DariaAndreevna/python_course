first_lst = [1,2,3,4,5]
if len(first_lst) != 0:
    x = first_lst[-1]
    first_lst.insert(0, x)
    first_lst = first_lst[:-1]
print(first_lst)
