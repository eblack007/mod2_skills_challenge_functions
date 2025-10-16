from lib.estimate_reading_time import estimate_reading_time
import pytest
"""
Given a test containing zero words
It should return zero minutes and zero seconds
"""
def test_estimate_reading_time_given_empty_string():
    assert estimate_reading_time('') == '0 minutes 0 seconds'

"""
Given a text containing a certain number of words
Return the time in minutes and seconds it would take to read the text at 200 wpm
"""

def test_estimate_reading_time_given_a_text():
    assert estimate_reading_time('A long time ago in a galaxy far away,' \
    ' a jedi blew up the death star and destroyed the empire.') == '0 minutes 6 seconds'

def test_estimate_reading_time_given_not_a_string():
    with pytest.raises(Exception) as e:
        estimate_reading_time(7)
    error_message = str(e.value)
    assert error_message == 'Must pass a string to this function'

