# Without using sys and work quickly

def fact(n):
    result = 1
    while n != 0:
        result *= n
        n -= 1
    return result

import time
start = time.time()
print(fact(1000))
end = time.time()
print(end - start)