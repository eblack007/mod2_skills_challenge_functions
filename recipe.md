# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can manage my time
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
def estimate_reading_time(text):
    """
    Provides an estimated time to read a text at 200 wpm

    Parameters: text - a string (e.g. 'Hello world, I am from mars')

    Returns: a time in minutes and seconds to read the provided text

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    """
    pass
# EXAMPLE

```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
"""
given a test containing zero words
it should return zero minutes and zero seconds
"""
def test_estimate_reading_time_given_empty_string():
    assert estimate_reading_time('') == '0 minutes 0 seconds'

```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]
```

Ensure all test function names are unique, otherwise pytest will ignore them!
