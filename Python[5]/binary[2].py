#TODO: Binary search (big o notation)
def binsearch(x, n, s):
    low, high = 0, n - 1
    cnt = 0
    while low <= high:
        mid = (low + high) // 2
        cnt += 1
        if s[mid] == x:
            return cnt
        elif x < s[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return cnt

def solve(n, m, s, x):
    total = 0
    for i in range(m):
        total += binsearch(x[i], n, s)
    print(total, end ='')

N,M = map(int, input().split())
S = list(map(int, input().split()))
X = list(map(int, input().split()))
solve(N, M, S, X)

# Input:
# N, M = 8 7
# S = 11 17 26 28 37 45 53 59
# X = 33 28 64 53 81 26 11
# Output: 21

# Input 2:
# N, M = 10 10
# S = 17 46 49 62 66 76 78 79 84 98
# X = 78 46 66 79 49 84 17 76 98 62
# Output : 29

#TODO: binary search with recursive function
def binsearch(low, high, x, s):
    if low > high:
        return 0
    else:
        mid = (low + high) // 2
        if s[mid] == x:
            return 1
        elif x < s[mid]:
            return 1 + binsearch(low, mid - 1, x, s)
        else:
            return 1 + binsearch(mid + 1, high, x, s)
        
def solve(n , m, s ,x):
    total = 0
    for i in range(m):
        total += binsearch(0, n - 1, x[i], s)
    print(total)


N, M = map(int, input().split())
S = list(map(int, input().split()))
X = list(map(int, input().split()))
solve(N, M, S, X)