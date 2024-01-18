import sys
n, k = map(int, sys.stdin.readline().split())
coinList = []
count = 0

for i in range(n):
  coinList.append(int(sys.stdin.readline().rstrip()))

while k > 0:
  try:
    money = coinList.pop()
    count += k // money
    k -= money * (k // money)

  except:
    break

print(count)