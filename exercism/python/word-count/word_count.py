import re


def count_words(sentence: str):
    words = re.findall("[a-zA-Z0-9\']+", sentence.lower())
    counts = {}
    for i in [word.strip("\'") for word in words if word.strip("\'")]:
        counts[i] = counts.get(i, 0) + 1
    return counts
