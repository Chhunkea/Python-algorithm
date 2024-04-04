# Run much faster.

def gcd(n, m):
    while m != 0:
        n, m = (m, n % m)
    return n

n = 2451966000072168
m = 485897929014301292
print(gcd(n, m))