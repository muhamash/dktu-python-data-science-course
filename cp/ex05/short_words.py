"""Exercise 5.5. short words."""


def short_words(words: str, max_len: int) -> str:
    """Return a string of words that are shorter than max_len.

    :param words: string of words
    :param max_len: maximum length of words
    :return: string of words that are shorter than max_len
    """
    # TODO: Code has been removed from here.
    short_words = []
    for word in words.split():
        # for w in word:
        #     print(w)
        # print(word)
        if len(word) < max_len:
            short_words.append(word)
    # print(short_words)
    return " ".join(short_words)


s = "this is a sentence with some short and some longlonglong words"
print(short_words(s, 10))
