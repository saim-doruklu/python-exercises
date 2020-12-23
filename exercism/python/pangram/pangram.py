import re


def is_pangram(sentence):
    sentence = re.sub("\s", "", sentence)
    if not re.fullmatch("[a-z]+", sentence):
        return False
    return ''.join(set(sentence)).__len__() == 26
