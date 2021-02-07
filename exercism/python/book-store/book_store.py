# 1 -> 0
# 2 -> 5
# 3 -> 10
# 4 -> 20
# 5 -> 25
import sys

previously_calculated = dict()
discounts = {
    1: 0,
    11: 2 * 5,
    111: 3 * 10,
    1111: 4 * 20,
    11111: 5 * 25
}


def calculate_max_discount(counts, discount=0):
    if counts < 0:
        return None
    already_calculated = previously_calculated.get(counts)
    if already_calculated is not None:
        return already_calculated

    return max(counts)


def total(basket: list):
    as_string = "".join(sorted([str(basket.count(book)) for book in set(basket)]))
    counts = int(as_string)
    calculate_max_discount(counts)
