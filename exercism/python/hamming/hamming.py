def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Lengths are not equal")
    # print([[elements[1], elements[2]] for elements in zip(strand_b, strand_a, strand_a)])
    print(list(map(lambda a,b: a+b, strand_a,strand_b)))
    return len([1 for index in range(len(strand_a)) if strand_b[index] != strand_a[index]])
