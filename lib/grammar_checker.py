def grammar_checker(text):
    if len(text) < 1:
        return False
    ending_punctuation = ['!', '?', '.']
    if text[0].isupper() and text[-1] in ending_punctuation:
        return True
    else:
        return False