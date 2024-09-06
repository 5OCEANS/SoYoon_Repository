import sys

N = int(sys.stdin.readline())
shirtList = list(map(int, sys.stdin.readline().strip().split()))
T, P = map(int, sys.stdin.readline().strip().split())

shirtCount = 0

for i in range(6):
  if shirtList[i] % T == 0:
    shirtCount += shirtList[i] // T
  else:
    shirtCount += ((shirtList[i] // T) + 1)

print(shirtCount)
print(N//P, N % P)
