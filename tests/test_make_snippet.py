from lib.make_snippet import make_snippet
import pytest

def test_make_snippet_my_name():
    assert make_snippet('Hello my name is euan black') == 'Hello my name is euan ...'

def test_return_four_word_string():
    assert make_snippet('A big red house') == 'A big red house'

def test_make_snippet_start_of_book():
    assert make_snippet('A long time ago in a galaxy far away') == 'A long time ago in ...'

def test_make_snippet_takes_only_string():
    with pytest.raises(Exception) as e:
        make_snippet(6)
    error_message = str(e.value)
    assert error_message == 'Must pass a string to this function'

def test_make_snippet_if_given_empty_string_returns_empty_string():
    assert make_snippet('') == ''

def test_given_string_delimitted_by_commas():
    assert make_snippet('one,two,three,four,five,six') == 'one,two,three,four,five,six'