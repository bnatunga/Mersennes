#Lucas-Lehmer sequence up to i = p − 2 (inclusive)
def lucas_lehmer(p):
    lucas = [4]
    for x in range(1, p-1):
        lucas.append((lucas[x-1]**2 - 2)%(2**p - 1))
    return lucas

print(lucas_lehmer(17))

#mersenne_primes(the number is prime if the Lucas-Lehmer series is 0 at position p − 2
def ll_prime(p):
    lucas = [4]
    for x in range(1, p):
        lucas.append((lucas[x-1]**2 - 2)%(2**p - 1))
        if lucas[p-2] == 0:
            return True
        return False