def second_index(text: str, some_str: str) -> int or None:

    if text.count(some_str) <= 1:
        return None
    ind = text.find(some_str)
    ind = text.find(some_str, ind + 1)
    return ind


assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
assert second_index("Bye bye", "s") is None, 'Test5'
print('ОК')
