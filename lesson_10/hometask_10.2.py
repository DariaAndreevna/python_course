import string


def first_word(text: str) -> str:
    """ First word searching
    :param text: certain text
    :return: first word in the text
    """
    for p in string.punctuation:
        if p == "'":
            text = text
        else:
            text = text.replace(p, " ")
    text = text.strip().split(" ")
    return text[0]


assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
print('OK')
