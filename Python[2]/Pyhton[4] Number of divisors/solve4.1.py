# Measuring the time its take
def solve(N):
    cnt = 0
    for i in range(1, N + 1):
        if N % i == 0:
            cnt += 1
    return cnt    
N = int(input())

import time 
start = time.time()
print(solve(N))
end = time.time()
print(f'solve() elapsed time : {end - start}')
