def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)

import time
start = time.time()
print(fact(100))
end = time.time()
print(end - start)

# limited the factorial
import sys
print(sys.getrecursionlimit())

sys.setrecursionlimit(10 ** 5)
print(sys.getrecursionlimit())