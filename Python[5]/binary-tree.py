# TODO: Binary Search: [7] Cutting Trees
# Recursion

def cut(n, s, h):
    length = 0
    for i in range(n):
        length += (s[i] - h) if s[i] > h else 0
    return length

def binsearch(low, high, n, m, s):
    if low > high:
        return low - 1
    else:
        mid = (low + high) // 2
        if cut(n, s, mid) < m:
            return binsearch(low, mid - 1, n, m, s)
        else:
            return binsearch(mid + 1, high, n, m, s )
        
def solve(n, m, s):
    j = binsearch(0, max(s), n, m, s)
    print(j)

N, M = map(int, input().split())
S = list(map(int, input().split()))
solve(N, M, S)

# Input1:
# N, M = 4 7
# S = 20 15 10 17
# Output: 15

# Input2:
# N, M = 5 20
# S = 4 42 40 26 46
# Output: 36


# TODO: Binary Search: [7] Cutting Trees
# Iteration

def cut(n, s, h):
    length = 0
    for i in range(n):
        length += (s[i] - h) if s[i] > h else 0
    return length

def binsearch(n, m, s):
   low, high = 0, max(s)
   while low < high:
       mid = (low + high) // 2
       if cut(n, s, mid) < m:
           high = mid
       else:
           low = mid + 1
   return low - 1

def solve(n, m, s):
    j = binsearch(n, m, s)
    print(j)

N, M = map(int, input().split())
S = list(map(int, input().split()))
solve(N, M, S)

# Input1:
# N, M = 4 7
# S = 20 15 10 17
# Output: 15

# Input2:
# N, M = 5 20
# S = 4 42 40 26 46
# Output: 36
