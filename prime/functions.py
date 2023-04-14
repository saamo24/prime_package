def is_prime(num):
    if num < 2:
        return False
    for n in range(2, int(num**0.5)+1):
        if num % n == 0:
            return False
    return True


def prime_range(n):
    for i in range(2, n):
        if is_prime(i):
            yield i

def factors(n):
    for i in range(1, n+1):
        if n % i == 0:    
            yield i

def prime_factors(num):
    for i in factors(num):
        if is_prime(i):
            yield i