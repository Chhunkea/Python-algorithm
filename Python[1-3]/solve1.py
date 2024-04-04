# TODO: Python Algorithm (Matrix)

def mprint(A):
    n, m = len(A), len(A[0])
    for i in range(n):
        for j in range(m):
            print(A[i][j], end = ' ')
        print()

def madd(A, B):
    n, m = len(A), len(A[0])
    C = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for j in range(m):
                C[i][j] = A[i][j] + B[i][j]
    return C
    
N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]
C = madd(A, B)
mprint(C)

# input: 2 2 1 2 3 4 5 6 7 8
# n = 2, m = 2
# so it count (1 2 3 4) + (5 6 7 8)
# Output: 6 8 10 12
