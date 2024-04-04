#TODO: Prime number Determination

# [Prime] number is a number that divide with (1 and itself)
# [Composite] number is a number that divide with (many number) 

#Code with flowchart
def solve(n):
    if n <= 1:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

N = int(input())

import time 
start = time.time()
print('Yes' if solve(N) else 'No')
end = time.time()
print(f'solve() elapsed time: {end - start}')