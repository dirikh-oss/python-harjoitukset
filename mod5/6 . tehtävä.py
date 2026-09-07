import random

N = int(input("Pisteiden määrä: "))
n = sum(1 for _ in range(N) if random.uniform(-1, 1)**2 + random.uniform(-1, 1)**2 < 1)

print(f"Pii: {4 * n / N}")