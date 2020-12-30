import re


class Luhn:
    def __init__(self, card_num: str):
        if not re.fullmatch("[\s\d]+", card_num):
            self.is_valid = False
        else:
            card_num = re.sub("\s", "", card_num)
            if len(card_num) <= 1:
                self.is_valid = False
            else:
                sum = 0
                for index, digit in enumerate(reversed(card_num)):
                    if index % 2 == 0:
                        sum += int(digit)
                    else:
                        this_digit = 2 * int(digit)
                        if this_digit > 9:
                            this_digit -= 9
                        sum += this_digit
                self.is_valid = sum % 10 == 0

    def valid(self):
        return self.is_valid
