import sys

N = int(sys.stdin.readline())
priceList = list()

for _ in range(N):
  price = int(sys.stdin.readline())
  priceList.append(price)

ans = 0
M = int(sys.stdin.readline())
for i in range(M):
  num = int(sys.stdin.readline())
  ans += priceList[num-1]

print(ans)