#TODO: Number of divisors

# quiz (divisor 8 form 1 to 8)
print(8 / 1)

# Code in pyhton (my code)
N = int(input())
cnt = 0
for i in range(1, N + 1):
    if N % i == 0:
        cnt += 1
print(cnt)

# Computer code
def solve(N):
    cnt = 0
    for i in range(1, N + 1):
        if N % i == 0:
            cnt += 1
    return cnt    
N = int(input())
print(solve(N))

# input: 10
# Output: 3
# its count the divisor of 10 (1, 2, 5 ,10)