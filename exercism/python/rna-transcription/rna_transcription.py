matches = {
    "C": "G",
    "G": "C",
    "A": "U",
    "T": "A"
}


def to_rna(dna_strand):
    return "".join([matches[letter] for letter in dna_strand])
