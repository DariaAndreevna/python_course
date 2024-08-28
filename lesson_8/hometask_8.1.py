def add_one(some_list: list) -> list:
    new_str = "".join([str(el) for el in some_list])
    new_str = int(new_str)
    sum_int = new_str + 1
    sum_int = str(sum_int)
    return [int(num) for num in sum_int]


assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")
