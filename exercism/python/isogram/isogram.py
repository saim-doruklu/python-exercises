import re


def is_isogram(string:str):
    letters = re.findall("[a-z]", string.lower())
    return len(letters) == len(set(letters))
