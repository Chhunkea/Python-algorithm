#TODO: Asymptotic analysis

def solve(n, s):
    maxn, maxi = s[0], 0
    for i in range(1, n):
        if maxn < s[i]:
            maxn, maxi = s[i], i
    return maxn, maxi

n = int(input())
s = list(map(int, input().split()))
maxn, maxi = solve(n, s)
print(maxn, maxi)

# Output:
# 5 so at this point it take only five integer
# 10 20 30 40 50 60
# output 50 4  (its only count the largest number and four is the index where 50 located)