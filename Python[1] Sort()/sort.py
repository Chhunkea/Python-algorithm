import random

SEED, MIN, MAX, N = 2024, 10, 100, 4
random.seed(SEED)
S = random.sample(range(MIN, MAX), N)

print(S)
print(sorted(S))