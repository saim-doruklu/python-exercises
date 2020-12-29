import re


def abbreviate(words: str):
    return "".join([word.group()[0] for word in re.finditer("(([a-zA-Z0-9]+)('[a-zA-Z0-9]+)?)", words.upper())])
