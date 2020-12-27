from functools import reduce


def is_armstrong_number(number):
    if number == 0:
        return True
    single_digits = map(int, str(number))
    each_digit_to_the_power_number_len = map(lambda n: n ** str(number).__len__(), single_digits)
    sum_all = reduce(lambda a, b: a + b, each_digit_to_the_power_number_len, 0)
    return number == sum_all
