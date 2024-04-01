#  Use this code for time improvement
def solve(n):
    cnt = 0
    sqrt = int(n ** 0.5)
    for i in range(1, sqrt + 1):
        if n % i == 0:
            cnt += 2
    if sqrt * sqrt == n:
        cnt -= 1
    return cnt
N = int(input())

import time 
start = time.time()
print(solve(N))
end = time.time()
print(f'solve() elapsed time : {end - start}')

# sqrt is the root that it takes