from lib.count_words import count_words

"""
A function called count_words that takes a string as an argument
and returns the number of words in that string.
"""

def test_count_words_given_empty_string():
    assert count_words('') == 0

def test_count_words_given_string():
    assert count_words('Hello world') == 2

