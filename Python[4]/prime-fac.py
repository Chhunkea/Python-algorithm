# TODO: 4. Sequential Search: [4] Prime Factorization

def is_fac(n):
    if n < 2:
        return []
    else:
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return [i] + is_fac(n//i)
        return [n]

def solve(n):
    factors = is_fac(n)
    print('.'.join(map(str, factors)))    

N = int(input())
solve(N)
