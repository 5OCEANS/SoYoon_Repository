import sys, math

N = int(sys.stdin.readline())
threeCount = 0
twoCount = 0
oneCount = 0
ans = 0
for i in range(N):
  amount = sys.stdin.readline().strip()
  if amount == '1/4':
    oneCount += 1
  elif amount == '1/2':
    twoCount += 1
  elif amount == '3/4':
    threeCount += 1

ans += threeCount
if oneCount >= threeCount:
  oneCount -= threeCount
else:
  oneCount = 0
ans += (twoCount // 2)
if twoCount % 2 == 1: # 남은 1/2판이 있다면
  if oneCount == 0:
    ans += 1
  elif oneCount > 0:
    if oneCount < 3:
      ans += 1
      oneCount = 0
    else:
      ans += 1
      oneCount -= 2
ans += math.ceil(oneCount / 4)
print(ans)