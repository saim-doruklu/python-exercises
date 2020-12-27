codon_to_amino_acid = {
    "AUG": "Methionine",
    "UUU": "Phenylalanine",
    "UUC": "Phenylalanine",
    "UUA": "Leucine",
    "UUG": "Leucine",
    "UCU": "Serine",
    "UCC": "Serine",
    "UCA": "Serine",
    "UCG": "Serine",
    "UAU": "Tyrosine",
    "UAC": "Tyrosine",
    "UGU": "Cysteine",
    "UGC": "Cysteine",
    "UGG": "Tryptophan",
    "UAA": "STOP",
    "UAG": "STOP",
    "UGA": "STOP",
}


def codon_to_amino_acid_generator(nucleotids) -> iter:
    for j in range(0, len(nucleotids), 3):
        codon = nucleotids[j: j + 3]
        amino_acid_or_stop = codon_to_amino_acid.get(codon)
        if amino_acid_or_stop == "STOP":
            return
        if amino_acid_or_stop is not None:
            yield amino_acid_or_stop


def proteins(strand):
    return list(codon_to_amino_acid_generator(strand))
