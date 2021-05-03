def mersenne_number(p):
    return 2**p - 1


#calculate mersenne numbers of primes in range
def is_prime(number):
    if number <= 1:
        return False
    for factor in range(2,number):
        if number%factor == 0:
            return False
        return True

def get_primes(n_start, n_end):
    primes =[]
    for number in range(n_start, n_end):
        if is_prime(number):
            primes.append(number)
        return primes

primes_btn= get_primes(3, 65)

mersennes = []
for p in primes_btn:
    mersennes.append(2**p - 1)
mersennes