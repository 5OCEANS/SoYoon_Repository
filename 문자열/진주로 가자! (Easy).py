import sys

N = int(sys.stdin.readline())

jinju_price = 0
expensive_price_count = 0
other_price = []

for i in range(N):
  D, C = sys.stdin.readline().strip().split()

  if D == 'jinju':
    jinju_price = int(C)

  other_price.append(C)

print(jinju_price)

for i in other_price:
  if jinju_price < int(i):
    expensive_price_count += 1

print(expensive_price_count)