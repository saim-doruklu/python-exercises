from __future__ import division

import math


class Rational:
    primes = [2]
    max_number_checked_for_prime = 2

    def __init__(self, numer, denom, numer_factors=None, denom_factors=None):
        self.sign = -1 if (numer < 0 < denom) or (numer > 0 > denom) else 1
        if numer == 0:
            self.numer = 0
            self.denom = 1
            self.numerator_factors = []
            self.denominator_factors = []
            return

        if numer < 0:
            numer *= -1
        if denom < 0:
            denom *= -1

        if numer_factors is not None and denom_factors is not None:
            self.numerator_factors = numer_factors
            self.denominator_factors = denom_factors
            self.numer = numer
            self.denom = denom
        else:
            self.calculate_primes_up_to_sqrt_of(max(numer, denom))

            self.numerator_factors = self.factor(numer)
            self.denominator_factors = self.factor(denom)
            self.eliminate_common_divisors(self.numerator_factors, self.denominator_factors)

            self.numer = self.calculate_num_from_factors(self.numerator_factors)
            self.denom = self.calculate_num_from_factors(self.denominator_factors)

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        numer_one = self.numer
        numer_two = other.numer
        sign_one = self.sign
        sign_two = other.sign
        denom_one = self.denom
        denom_two = other.denom
        denom_factors_one = self.denominator_factors.copy()
        denom_factors_two = other.denominator_factors.copy()
        numer_factors_one = self.numerator_factors.copy()
        numer_factors_two = other.numerator_factors.copy()

        return self.add_with_params(numer_factors_one, numer_factors_two, denom_factors_one, denom_factors_two,
                                    denom_one, denom_two, numer_one, numer_two,
                                    sign_one, sign_two)

    def __sub__(self, other):
        numer_one = self.numer
        numer_two = other.numer
        sign_one = self.sign
        sign_two = other.sign * -1
        denom_one = self.denom
        denom_two = other.denom
        denom_factors_one = self.denominator_factors.copy()
        denom_factors_two = other.denominator_factors.copy()
        numer_factors_one = self.numerator_factors.copy()
        numer_factors_two = other.numerator_factors.copy()

        return self.add_with_params(numer_factors_one, numer_factors_two, denom_factors_one, denom_factors_two,
                                    denom_one, denom_two, numer_one, numer_two,
                                    sign_one, sign_two)

    def __mul__(self, other):
        if self.numer == 0 or other.numer == 0:
            return Rational(0, 1)
        num_factors_one = self.numerator_factors.copy()
        denom_factors_one = self.denominator_factors.copy()
        num_factors_two = other.numerator_factors.copy()
        denom_factors_two = other.denominator_factors.copy()
        sign = self.sign * other.sign

        return self.multiply_with_calculated_factors(denom_factors_one, denom_factors_two, num_factors_one,
                                                     num_factors_two, sign)

    def __truediv__(self, other):
        if self.numer == 0:
            return Rational(0, 1)
        if other.numer == 0:
            raise ArithmeticError("Division by zero")

        num_factors_one = self.numerator_factors.copy()
        denom_factors_one = self.denominator_factors.copy()
        reverse_num_factors_two = other.denominator_factors.copy()
        reverse_denom_factors_two = other.numerator_factors.copy()
        sign = self.sign * other.sign

        return self.multiply_with_calculated_factors(denom_factors_one, reverse_denom_factors_two, num_factors_one,
                                                     reverse_num_factors_two, sign)

    def __abs__(self):
        pass

    def __pow__(self, power):
        pass

    def __rpow__(self, base):
        pass

    def eliminate_common_divisors(self, factors_one, factors_two):
        common_primes = []
        for prime in factors_one:
            if prime in factors_two:
                common_primes.append(prime)

        for prime in common_primes:
            power_of_prime_in_num_one = factors_one[prime]
            power_of_prime_in_num_two = factors_two[prime]
            min_power = min(power_of_prime_in_num_two, power_of_prime_in_num_one)

            power_of_prime_in_num_one -= min_power
            power_of_prime_in_num_two -= min_power

            if power_of_prime_in_num_two == 0:
                factors_two.__delitem__(prime)
            else:
                factors_two[prime] = power_of_prime_in_num_two

            if power_of_prime_in_num_one == 0:
                factors_one.__delitem__(prime)
            else:
                factors_one[prime] = power_of_prime_in_num_one

    def factor(self, number: int):
        factors = {}

        number_copy = number
        for prime in Rational.primes:
            if prime * prime > number:
                break
            can_be_divided_to_the_power_prime = 0
            while number_copy % prime == 0:
                can_be_divided_to_the_power_prime += 1
                number_copy = number_copy // prime
            if can_be_divided_to_the_power_prime > 0:
                factors[prime] = can_be_divided_to_the_power_prime

        if number_copy > 1:
            factors[number_copy] = 1
        return factors

    def calculate_primes_up_to_sqrt_of(self, number):
        while Rational.max_number_checked_for_prime * Rational.max_number_checked_for_prime < number:
            marked_non_prime = set()
            for prime in Rational.primes:
                next_marked = prime * (Rational.max_number_checked_for_prime // prime + 1)
                while next_marked <= Rational.max_number_checked_for_prime * 2:
                    marked_non_prime.add(next_marked)
                    next_marked += prime
            for i in range(Rational.max_number_checked_for_prime + 1, Rational.max_number_checked_for_prime * 2 + 1):
                if i not in marked_non_prime:
                    Rational.primes.append(i)
            Rational.max_number_checked_for_prime = Rational.max_number_checked_for_prime * 2

    def minimum_common_multiple(self, factors_one: dict, factors_two: dict):
        factors_of_common_multiple = factors_one
        for factor, power in factors_two.items():
            power_of_same_factor_in_other = factors_of_common_multiple.get(factor)
            if power_of_same_factor_in_other is None or power > power_of_same_factor_in_other:
                factors_of_common_multiple[factor] = power
        common_multiple = self.calculate_num_from_factors(factors_of_common_multiple)
        return common_multiple

    def add_with_params(self, numer_factors_one, numer_factors_two, denom_factors_one, denom_factors_two, denom_one,
                        denom_two, numer_one, numer_two,
                        sign_one, sign_two):
        if numer_one == 0:
            return Rational(sign_two * numer_two, denom_two, numer_factors_two, denom_factors_two)
        if numer_two == 0:
            return Rational(sign_one * numer_one, denom_one, numer_factors_one, denom_factors_one)

        minimum_common_multiple = self.minimum_common_multiple(denom_factors_one, denom_factors_two)
        numer_one = numer_one * (minimum_common_multiple // denom_one)
        numer_two = numer_two * (minimum_common_multiple // denom_two)
        numerator_sum = numer_one * sign_one + numer_two * sign_two
        return Rational(numerator_sum, minimum_common_multiple)

    def calculate_num_from_factors(self, factors):
        calculation = 1
        for item in factors.items():
            calculation *= item[0] ** item[1]
        return calculation

    def multiply_factors(self, num_factors_one: dict, num_factors_two: dict):
        for factor, power_of_factor_in_num_two in num_factors_two.items():
            power_of_factor_in_num_one = num_factors_one.get(factor) or 0
            num_factors_one[factor] = power_of_factor_in_num_one + power_of_factor_in_num_two
        return num_factors_one


    def multiply_with_calculated_factors(self, denom_factors_one, denom_factors_two, num_factors_one, num_factors_two,
                                         sign):
        self.eliminate_common_divisors(num_factors_one, denom_factors_two)
        self.eliminate_common_divisors(num_factors_two, denom_factors_one)
        multiplied_numer_factors = self.multiply_factors(num_factors_one, num_factors_two)
        multiplied_denom_factors = self.multiply_factors(denom_factors_one, denom_factors_two)
        numer = self.calculate_num_from_factors(multiplied_numer_factors)
        denom = self.calculate_num_from_factors(multiplied_denom_factors)
        numer *= sign
        return Rational(numer, denom, multiplied_numer_factors, multiplied_denom_factors)