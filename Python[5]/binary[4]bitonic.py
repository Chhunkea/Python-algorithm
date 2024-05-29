# TODO: Binsearch [4] Bitonic sequence
# Recursion

def binsearch(low, high, n, s):
    mid = (low + high) // 2
    if mid == 0 or mid > (n - 1):
        return -1
    else:
        if s[mid-1] < s[mid] > s[mid+1]:
            return mid
        elif s[mid-1] < s[mid] < s[mid+1]:
            return binsearch(mid + 1, high, n, s)
        else:
            return binsearch(low, mid - 1, n, s)
        

def solve(n, s):
    j = binsearch(0, n - 1, n, s)
    print(j, s[j])

N = int(input())
S = list(map(int, input().split()))
solve(N, S)

# Input1:
# N = 7
# 18 27 42 82 73 67 25
# Output: 3 82

# Input2:
# N = 9
# 27 44 57 69 88 96 53 33 10
# Output: 5 96

# Input3:
# N = 10
# 17 95 87 56 49 42 37 31 21 20
# Output: 1 95

# Solution 2 (Iteration)

def binsearch(n, s):
    low, high = 0, n - 1
    mid = (low + high) // 2
    while mid != 0 and mid != n - 1:
        mid = (low + high) // 2
        if s[mid-1] < s[mid] > s[mid+1]:
            return mid
        elif s[mid-1] < s[mid] < s[mid+1]:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def solve(n, s):
    j = binsearch(n, s)
    print(j, s[j])

N = int(input())
S = list(map(int, input().split()))
solve(N, S)