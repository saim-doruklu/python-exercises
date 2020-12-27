import random
from string import ascii_uppercase

ALPHABET = list(ascii_uppercase)
UNIQUE_NAMES = set()


def random_letter_producer(): return ALPHABET[random.randint(0, ALPHABET.__len__() - 1)]


def random_digit_producer(): return str(random.randint(0, 9))


def n_char_producer(n, char_producer):
    if n == 0:
        return ""
    return n_char_producer(n - 1, char_producer) + char_producer()


def random_char_digit_combination_producer():
    return n_char_producer(2, random_letter_producer) + n_char_producer(3,
                                                                        random_digit_producer)


def name_collision_checker(potential_name):
    return not UNIQUE_NAMES.__contains__(potential_name)


def unique_names_updater(name):
    UNIQUE_NAMES.add(name)


def valid_string_producer(string_producer, string_validity_checker, invalid_case_handler, valid_case_handler):
    name = string_producer()
    if not string_validity_checker(name):
        return invalid_case_handler()
    else:
        valid_case_handler(name)
        return name


def unique_random_name_creator():
    return valid_string_producer(random_char_digit_combination_producer, name_collision_checker,
                                 unique_random_name_creator,
                                 unique_names_updater)


class Robot:
    def __init__(self):
        self.name = unique_random_name_creator()

    def reset(self):
        self.__init__()
