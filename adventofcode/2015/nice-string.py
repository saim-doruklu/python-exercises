import re


def part_one(strings):
    count = 0
    for a_string in strings:
        if len(re.findall('[aeiou]', a_string)) < 3:
            continue
        if not re.findall('(.)\\1', a_string):
            continue
        if re.findall('ab|cd|pq|xy', a_string):
            continue
        count += 1
    return count


def part_two(strings):
    count = 0
    for a_string in strings:
        if len(re.findall('(..).*\\1', a_string)) == 0:
            continue
        if len(re.findall('(.).\\1', a_string)) == 0:
            continue
        count += 1
    return count


if __name__ == '__main__':
    with open('inputs/nice-string.txt', 'r') as file:
        all_lines = file.readlines()
        count_part_one = part_one(all_lines)
        count_part_two = part_two(all_lines)
        print(count_part_one)
        print(count_part_two)
        print(part_two(["aaxcbvbaa"]), 1)
        print(part_two(["aaa"]), 0)
        print(part_two(["aaaa"]), 1)
        print(part_two(["aaxaa"]), 1)
        print(part_two(["qjhvhtzxzqqjkmpb"]), 1)
        print(part_two(["uurcxstgmygtbstg"]), 0)
