"""Exercise 6.3-6.4."""


def word_histogram(lines: list) -> dict:
    """Return the word count histogram from the input lines.

    :param lines: The lines that are analyzed for word count.
    :return: The histogram of word occurrences.
    """
    # TODO: Code has been removed from here.
    word = {}
    for i in lines:
        words = i.lower().split()
        # print(words)
        for j in words:
            # print(j)
            if j.isalpha():
                if j in word:
                    word[j] = word[j] + 1
                else:
                    word[j] = 1
    return word


def extract_keyword(lines: str, ignore_list: list) -> dict:
    """Return the five most frequent words that are not on the ignore list and their occurrences.

    :param lines: The sentence to extract keywords from.
    :param ignore_list: The words that should ignored.
    :return: The five most frequent words in the sentence as keys with their count as values.
    """
    # TODO: Code has been removed from here.
    word_histogram = {}

    # print(f"lines core arg: {lines}")
    for i in lines:
        # print(i)
        words = i.lower().split()
        # print(word)

        for j in words:
            # print(j)
            if j.isalpha() and j not in ignore_list:
                if j in word_histogram:
                    word_histogram[j] += 1
                else:
                    word_histogram[j] = 1
    sorted_words = sorted(
        word_histogram.items(), key=lambda item: int(item[1]), reverse=True
    )
    # print(word_histogram)
    top_five = dict(sorted_words[:5])
    return top_five


if __name__ == "__main__":
    # here you can try out your functions
    lines = [
        "This is the first sentence of text for you",
        "This is the second sentence of text",
        "This is for you",
    ]
    print("word_histogram")
    print(word_histogram(lines))

    # Ignore list of common words
    ignore_list = ["the", "be", "to", "of", "and", "a", "in", "is", "have", "I"]

    # Print the 5 most occurring keywords
    print("extract_keywords")
    print(extract_keyword(lines, ignore_list))
