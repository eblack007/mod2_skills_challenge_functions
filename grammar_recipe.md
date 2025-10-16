# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can improve my grammar
I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
def estimate_reading_time(text):

    """
    Checks that a text starts with a capital letter and ends with a suitable-ending punctuation mark

    Parameters: text - a string 

    Returns: Boolean - True if text starts with capital letter and end with suitable punctuation mark.

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
