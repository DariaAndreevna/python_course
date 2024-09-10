from inspect import isgenerator
from math import sqrt


def is_prime(number: int) -> bool:
    """
    Checks if giving number is prime
    :param number: given number
    :return: bool with result
    """
    for divider in range(2, int(sqrt(number)) + 1):
        if number % divider == 0:
            return False
    return True


def prime_generator(end: int) -> callable([int]):
    """
    Sequence created from prime numbers
    :param end: the final number of sequence
    :return: result sequence
    """
    for number in range(2, end + 1):
        if is_prime(number):
            yield number


gen = prime_generator(1)
assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('Ok')
