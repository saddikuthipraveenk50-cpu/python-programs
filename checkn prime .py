def primes_range(n):
    primes = []
    for num in range(2, n+1):
        if all(num % i for i in range(2, int(num**0.5)+1)):
            primes.append(num)
    return primes

print(primes_range(30))
