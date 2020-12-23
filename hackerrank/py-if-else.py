#!/bin/python

def is_even(number):
    return number % 2 == 0


if __name__ == '__main__':
    n = int(input().strip())
    if not(is_even(n)):
        print("Weird")
    else:
        if (2 <= n) & (n <= 5):
            print("Not Weird")
        elif (6 <= n) & (n <= 20):
            print("Weird")
        else:
            print("Not Weird")
