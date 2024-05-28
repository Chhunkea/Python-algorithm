#TODO: Twenty QA game.
# Using iteration

def solve(x, s, t):
    low, high = s, t
    while low < high:
        mid = (low + high) // 2
        print(f'Bigger than {mid}?', end= ' ')
        if x > mid:
            print('Yes')
            low = mid + 1
        else:
            print('No')
            high = mid
    print(f'Your x is {low}')
    return low
        
import random
s, t = map(int, input().split())
SEED = int(input())
random.seed(SEED)
x = random.randint(s, t)
solve(x, s, t)

# Task 1
# Input s, t = 1, 100
# SEED = 2022
# output = 69

# Task 2
# Input s, t = 1, 1000000
# SEED = 2022
# output = 557451


# Twenty QA game.
#TODO: Using recursion

def solve(x, low, high):
    if low >= high :
        print(f'Your X is {low}.')
        return low
    else:
        mid = (low + high) // 2
        print(f'Bigger than {mid}?', end= ' ')
        if x > mid:
            print('Yes')
            return solve(x, mid + 1, high)
        else:
            print('No')
            return solve(x, low, mid)
        
import random
s, t = map(int, input().split())
SEED = int(input())
random.seed(SEED)
x = random.randint(s, t)
solve(x, s, t)