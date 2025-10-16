from lib.grammar_checker import grammar_checker

def test_check_grammar_checker_given_empty_string():
    assert grammar_checker('') == False

def test_grammar_checker_given_good_text():
    assert grammar_checker('Happy holidyas!') == True