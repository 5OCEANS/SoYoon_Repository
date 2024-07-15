import sys, math

N = int(sys.stdin.readline().strip())
A = list(map(int, sys.stdin.readline().strip().split()))
B, C = map(int, sys.stdin.readline().strip().split())

totalSecond = 0

for i in range(len(A)):
  if A[i] < B:
    second = 0
  else:
    second = (A[i] - B) // C if (A[i] - B) % C == 0 else math.floor((A[i] - B) / C) + 1
  totalSecond += second

print(totalSecond + N)