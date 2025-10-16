import math

def estimate_reading_time(text):
    if isinstance(text, str):
        word_count = len(text.split())
        time = word_count / 200
        minutes = math.floor(time)
        seconds = round((time - minutes) * 60)
        return f'{minutes} minutes {seconds} seconds'
        
    raise Exception('Must pass a string to this function')