"""Exercise 6.7: Sentiment analysis."""


def sentiment_analysis(text: str) -> int:
    """Return the sentence sentiment score, according to the rules of words scoring, as described in the text above.

    :param text: The sentence to check for sentiment scoring.
    :return: The total sentiment scoring of the sentence.
    """
    # TODO: Code has been removed from here.
    score = {
        "horrible": -5,
        "awful": -5,
        "bad": -4,
        "terrible": -4,
        "mediocre": -2,
        "lousy": -3,
        "poor": -3,
        "unfair": -1,
        "average": 0,
        "wonderful": +2,
        "beautiful": +3,
        "good": +3,
        "fantastic": +4,
        "excellent": +4,
        "superb": +4,
        "amazing": +4,
        "great": +4,
        "best": +5,
        "brilliant": +5,
    }

    words = text.split()
    # print(words)
    but_index = words.index("but")
    # print(words[but_index + 1 :])
    sentiment_score = 0
    for i in words[but_index + 1 :]:
        word_score = score.get(i, 0)
        # print(word_score)
        sentiment_score = sentiment_score + word_score
    return sentiment_score


if __name__ == "__main__":
    # here you can try out your functions
    text = "I think the food was excellent and great, but the service was horrible fgsdfg dgsg dgsdg dgsdg dgvsdg"
    # sentiment_analysis(text)
    print(sentiment_analysis(text))
