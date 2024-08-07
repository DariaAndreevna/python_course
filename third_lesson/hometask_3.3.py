first_lst = [1, 2, 3, 4, 5]
if len(first_lst) % 2 == 0:
    mid_lst = len(first_lst) // 2
else:
    mid_lst = len(first_lst) // 2 + 1
second_lst = [first_lst[:mid_lst], first_lst[mid_lst:]]
print(second_lst)
