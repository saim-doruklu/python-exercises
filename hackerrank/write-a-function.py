def is_divisible_by(year, divisor):
    return year % divisor == 0


def is_leap(year):
    leap = is_divisible_by(year,4)
    leap = leap and (is_divisible_by(year,400) or not(is_divisible_by(year,100)))

    return leap

if __name__ == '__main__':
    year = int(input())
    print(is_leap(year))