from inspect import isgenerator
from typing import Iterator


def pow(x: int) -> int:
    return x ** 2


def some_gen(begin: int, end: int, func) -> Iterator[int]:
    """
     Sequence created by some function
     begin: first element in sequence
     end: number elements in sequence
     func: function that forms value for sequence
     return: Iterator for the resulting sequence
    """
    previous_number = begin
    for i in range(end):
        yield previous_number
        previous_number = func(previous_number)


gen = some_gen(2, 4, pow)
assert isgenerator(gen) == True, 'Test1'
assert list(gen) == [2, 4, 16, 256], 'Test2'
print('OK')
