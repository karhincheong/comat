from collections import Counter
# Given a number, return the prime factors of that number


def prime_factorizer(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n = n // i
    if n > 2:
        factors.append(n)
    return factors


def format_prime_factorization(prime_factorization):
    # Prime factorization as a dict
    prime_factorization_dict = dict(Counter(prime_factorization))
    # Unicode for indexes
    indices = {"1": "¹", "2": "²", "3": "³", "4": "⁴", "5": "⁵", "6": "⁶", "7": "⁷", "8": "⁸", "9": "⁹", "0": "⁰"}
    multiplication_symbol = "×"
    # Iterate over prime_factorization_dict
    #
    def convert_to_superscript(prime_factorization_dict):
        # FIXME: Optimize time complexity
        new_index = ""
        for prime_factor in prime_factorization_dict:
            index = str(prime_factorization_dict[prime_factor])
            for digit in index:
                new_index.join(indices[digit])
        return new_index

