import re


def num_different_letters_in_str(some_str):
    return set(re.findall("[a-z]", some_str.lower())).__len__()


def is_pangram(sentence):
    return num_different_letters_in_str("The quick brown fox jumps over the lazy dog") == num_different_letters_in_str(
        sentence)
