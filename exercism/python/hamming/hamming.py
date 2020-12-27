def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Lengths are not equal")

    return sum([1 for index in range(len(strand_a)) if strand_b[index] != strand_a[index]])
