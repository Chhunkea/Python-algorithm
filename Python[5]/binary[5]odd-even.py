# TODO: Binary odd, even
# Recursion

def binsearch(low, high, n, s):
    if low == high:
        return -1 if s[low] % 2 == 1 else low
    else:
        mid = (low + high) // 2
        if s[mid] % 2 == 0: #even
            return binsearch(low, mid, n, s)
        else: #Odd
            return binsearch(mid + 1, high, n, s)
        
def solve(n, s):
    j = binsearch(0, n - 1, n, s)
    print(0 if j < 0 else s[j])

N = int(input())
S = list(map(int, input().split()))
solve(N, S)

# Input1:
# N = 7
# 7 3 1 9 8 4 2 6
# Output: 8

# Input2:
# N = 10
# 69 19 97 36 52 24 82 10 34 44
# Output: 36


# TODO: Binary odd, even
# Iteration

def binsearch(n, s):
    low, high = 0, n - 1
    while low <= high:
        mid = (low + high) // 2
        if s[mid] % 2 == 0: #even
            high = mid - 1
        else: #Odd
            low = mid + 1
    return -1 if s[low] % 2 == 1 else low
        
def solve(n, s):
    j = binsearch(n, s)
    print(0 if j < 0 else s[j])

N = int(input())
S = list(map(int, input().split()))
solve(N, S)

# Input1:
# N = 7
# 7 3 1 9 8 4 2 6
# Output: 8

# Input2:
# N = 10
# 69 19 97 36 52 24 82 10 34 44
# Output: 36
