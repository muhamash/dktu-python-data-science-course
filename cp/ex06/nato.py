"""Exercise 6.1: The NATO alphabet."""


def text_to_nato(plaintext: str) -> str:
    """Return the NATO version of a word separated by dashes.

    :param plaintext: The word to replace with its phrase according to the NATO alphabet.
    :return: The NATO representation of the input word.
    """
    # TODO: Code has been removed from here.
    alphabet_to_nato = {
        "a": "Alpha",
        "b": "Bravo",
        "c": "Charlie",
        "d": "Delta",
        "e": "Echo",
        "f": "Foxtrot",
        "g": "Golf",
        "h": "Hotel",
        "i": "India",
        "j": "Juliet",
        "k": "Kilo",
        "l": "Lima",
        "m": "Mike",
        "n": "November",
        "o": "Oscar",
        "p": "Papa",
        "q": "Quebec",
        "r": "Romeo",
        "s": "Sierra",
        "t": "Tango",
        "u": "Uniform",
        "v": "Victor",
        "w": "Whiskey",
        "x": "Xray",
        "y": "Yankee",
        "z": "Zulu",
    }

    nato = ""

    for i in plaintext.lower():
        # print(i)
        # print(nato)
        if i.isalpha():
            nato += alphabet_to_nato.get(i) + "-"
        else:
            nato = nato + i + " "
    return nato.rstrip("-")


if __name__ == "__main__":
    # here you can try out your functions
    print(text_to_nato("hello"))
