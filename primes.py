# function to calculate all prime numbers using dynamic programming
def prime(n):
    primes = [True] * (n+1)
    primes[0] = primes[1] = False
    for i in range(2, int(n**0.5)+1):
        if primes[i]:
            # start from i*i because all numbers below i*i would have already been marked
            for j in range(i*i, n+1, i): 
                primes[j] = False
    return primes

primes = prime(100)
for i in range(1, 101):
    if primes[i]:
        print(i, end=' ')