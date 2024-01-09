import math
n, k = map(int, input().split())

if k < 0 or k > n:
  print(0)

res = int(math.factorial(n) / (math.factorial(k) * math.factorial(n-k)))

print(res)