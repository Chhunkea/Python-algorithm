# TODO: Binary [6] Nth Prime Number
# Iteration with sieve of erathoses

def find_prime(n):
    sieve = [0, 0] + [1] * (n - 1)
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i] == 1:
            for j in range(i * i, n + 1, i):
                sieve[j] = 0
    return [i for i in range(n) if sieve[i] == 1]


def binsearch(x, n, s):
    low, high = 0, n - 1
    while low <= high:
        mid = (low + high) // 2
        if x == s[mid]:
            return mid
        elif x < s[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1

def solve(n, s, maxn):
    primes = find_prime(maxn)
    for i in range(n):
        j = binsearch(s[i], len(primes), primes)
        print(j + 1, end = ' ')
    print()

N = int(input())
S = list(map(int, input().split()))
solve(N, S, 100000)

# Input1:
# N = 10
# S = 1 2 3 4 5 6 7 8 11 13
# Output: 0 1 2 0 3 0 4 0 5 6

# Input2:
# N = 8
# S = 127 75 739 173 411 257 543 863
# Output: 31 0 131 40 0 55 0 150


# TODO: Binary [6] Nth Prime Number
# Recursion 

def binsearch(low, high, x, s):
    if low > high:
        return -1
    else:
        mid = (low + high) // 2
        if x == s[mid]:
            return mid
        elif x < s[mid]:
            return binsearch(low, mid - 1, x, s)
        else:
            return binsearch(mid + 1, high, x, s)

def solve(n, s, maxn):
    primes = find_prime(maxn)
    for i in range(n):
        j = binsearch(0, len(primes) - 1, s[i], primes)
        print(j + 1, end = ' ')
    print()

N = int(input())
S = list(map(int, input().split()))
solve(N, S, 100000)

# Input1:
# N = 10
# S = 1 2 3 4 5 6 7 8 11 13
# Output: 0 1 2 0 3 0 4 0 5 6

# Input2:
# N = 8
# S = 127 75 739 173 411 257 543 863
# Output: 31 0 131 40 0 55 0 150