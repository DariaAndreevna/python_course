def popular_words(text: str, words: list[str]) -> dict[str, int]:
    """
    Determine the popularity of certain words in a text
    :param text: certain text
    :param words: words to define
    :return: a dictionary with words and the number of times they appear in the text
    """
    input_words = text.lower().split(" ")
    words_count = dict.fromkeys(words, 0)
    for word in input_words:
        if word in words:
            words_count[word] = words_count[word] + 1
    return words_count


assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''',['i', 'was', 'three', 'near']) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}, 'Test1'
print('OK')
