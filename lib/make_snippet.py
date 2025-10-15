def make_snippet(string):
    if not type(string) == str:
        raise Exception('Must pass a string to this function')
    string_tuple = string.split()
    if len(string_tuple) < 5:
        return string
    else:
        snippet = ' '.join(string_tuple[:5]) + ' ...'
        return snippet