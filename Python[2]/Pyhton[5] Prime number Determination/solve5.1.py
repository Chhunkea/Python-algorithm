# Flowchart improvement Code
def solve(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 5) + 1):
        if n % i == 0:
            return False
    return True

N = int(input())

import time 
start = time.time()
print('Yes' if solve(N) else 'No')
end = time.time()
print(f'solve() elapsed time: {end - start}')


