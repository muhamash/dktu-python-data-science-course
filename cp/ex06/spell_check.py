def spell_check(text: str, corrections: dict) -> str:
    """Return the corrected text for spelling errors according to a set of rules.

    :param text: The sentence to check for spelling.
    :param corrections: The dictionary of wrongly spelled words and their equivalent corrected version.
    :return: The correctly spelled sentence.
    """
    words = text.split()
    corrected_words = []

    for i in words:
        cleaned_word = "".join(filter(str.isalpha, i))  # check punctuation
        original_punctuation = i[len(cleaned_word) :]
        print(original_punctuation)  # Preserve punctuation
        cleaned_word_lower = cleaned_word.lower()  # Preserve original case
        corrected_word = corrections.get(cleaned_word_lower, cleaned_word)
        corrected_words.append(corrected_word + original_punctuation)

    return " ".join(corrected_words)


if __name__ == "__main__":
    # Here you can try out your functions
    corrections = {
        "apsolute": "absolute",
        "teh": "the",
        "acess": "access",
        "occured": "occurred",
        "exampel": "example",
    }
    text = "The apsolute acess to teh data occured in this exampel."

    print(spell_check(text, corrections))
