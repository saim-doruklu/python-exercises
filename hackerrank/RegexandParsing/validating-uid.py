import re

if __name__ == '__main__':
    num_lines = int(input())
    for curr_line in range(0, num_lines):
        line = input()
        is_length_10 = re.compile('[a-zA-Z0-9]{10}')
        has_two_uppercase = re.compile('.*[A-Z].*[A-Z].*')
        has_three_digits = re.compile('.*[0-9].*[0-9].*[0-9].*')
        no_repetition = re.compile('(?:([a-zA-Z\d])(?!.*\\1)){10}')
        if not is_length_10.match(line):
            print("Invalid")
        elif not has_two_uppercase.match(line):
            print("Invalid")
        elif not has_three_digits.match(line):
            print("Invalid")
        elif not no_repetition.match(line):
            print("Invalid")
        else:
            print("Valid")
