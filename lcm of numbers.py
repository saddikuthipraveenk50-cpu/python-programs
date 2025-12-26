def lcm(a, b):
    from math import gcd
    return a * b // gcd(a, b)

print(lcm(12, 18))
