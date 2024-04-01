#TODO: Python algorithm (Arbitrary natural number) 

def solve(N):
    s = 0
    for i in range(1, N + 1):
        s += i
    return s

N = int(input())
print(solve(N))


# Fastest one: 
def solve(n):
    return n * (n + 1) // 2

N = int(input())
print(solve(N))

# input: 10, output: 55