from collections import Counter

# Given a number, return the prime factorization of that number
def prime_factorization(n):
    if n == 0:
        # Special case 0
        return 0

    def base_factorization(n):
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
        return dict(Counter(factors))

    superscripts = {
        "0": "⁰",
        "1": "¹",
        "2": "²",
        "3": "³",
        "4": "⁴",
        "5": "⁵",
        "6": "⁶",
        "7": "⁷",
        "8": "⁸",
        "9": "⁹",
    }

    def convert_to_superscript(x):
        return "".join(superscripts[digit] for digit in str(x))

    base_factorization = base_factorization(n)
    formatted = {}
    out_string = ""
    for factor in base_factorization:
        formatted.update(
            {str(factor): convert_to_superscript(base_factorization[factor])}
        )
    for factor in formatted:
        out_string += factor + formatted[factor] + "×"
    return out_string[:-1]


def factor_list(n):
    factors = [i for i in range(1, n + 1) if not (n % i)]
    return factors


# Given a number, determine if it is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
