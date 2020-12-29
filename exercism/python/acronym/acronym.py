import re


def abbreviate(words: str):
    return "".join([word.group()[0] for word in re.finditer("(([\w[^_]]+)('[\w[^_]]+)?)", words.upper())])
