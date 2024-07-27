import sys

N = int(sys.stdin.readline())
arr = []

for i in range(N):
  num = float(sys.stdin.readline().strip())
  arr.append(num)

for i in range(1, N):
  arr[i] = max(arr[i], arr[i]*arr[i-1])

print('%0.3f' % max(arr))