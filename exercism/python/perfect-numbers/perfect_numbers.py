class PrimesCalculator:
    primes = [2]
    max_number_checked_for_prime = 2

    def calculate_primes_up_to_sqrt_of(self, number):
        while self.max_number_checked_for_prime * self.max_number_checked_for_prime < number:
            marked_non_prime = set()
            for prime in self.primes:
                next_marked = prime * (self.max_number_checked_for_prime // prime + 1)
                while next_marked <= self.max_number_checked_for_prime * 2:
                    marked_non_prime.add(next_marked)
                    next_marked += prime
            for i in range(self.max_number_checked_for_prime + 1, self.max_number_checked_for_prime * 2 + 1):
                if i not in marked_non_prime:
                    self.primes.append(i)
            self.max_number_checked_for_prime = self.max_number_checked_for_prime * 2


static_primes_calculator = PrimesCalculator()


def factor(number: int, primes: list):
    factors = {}

    number_copy = number
    for prime in primes:
        if prime * prime > number:
            break
        divided_by = []
        last_divided_by = 1
        while number_copy % prime == 0:
            if not divided_by:
                divided_by.append(1)
            last_divided_by *= prime
            divided_by.append(last_divided_by)
            number_copy = number_copy // prime
        if last_divided_by > 1:
            factors[prime] = divided_by

    if number_copy > 1:
        factors[number_copy] = [1, number_copy]
    return factors


def classify(number):
    if number <= 0:
        raise ValueError("Number should be greater than 0")
    if number == 1:
        return "deficient"
    static_primes_calculator.calculate_primes_up_to_sqrt_of(number)
    factors = list(factor(number, PrimesCalculator.primes).values())
    counters = [0] * factors.__len__()
    sum = 0
    while True:
        multiplication = 1
        for n in range(counters.__len__()):
            multiplication *= factors[n][counters[n]]
        if multiplication < number:
            sum += multiplication

        row = 0
        counters[row] += 1
        while counters[row] == factors[row].__len__():
            counters[row] = 0
            row += 1
            if row == counters.__len__():
                break
            counters[row] += 1
        if row == counters.__len__():
            break
    if sum > number:
        return "abundant"
    elif sum == number:
        return "perfect"
    else:
        return "deficient"
