"""Exercise 4.3: Checking if a word is a palindrome."""


def is_palindrome(word):
    # Convert the word to lowercase to ignore case sensitivity
    word = word.lower()

    # Reverse the word
    reversed_word = word[::-1]

    # Check if the original word and the reversed word are the same
    return word == reversed_word


# Test cases
print(is_palindrome("madam"))  # Output: True
print(is_palindrome("gentleman"))  # Output: False
