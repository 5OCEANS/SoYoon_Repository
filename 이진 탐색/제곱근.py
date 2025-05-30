import sys

n = int(sys.stdin.readline().strip())
low = 1
high = n

while 1:
  mid = (low + high) // 2
  if mid ** 2 == n:
    print(mid)
    break
  elif mid ** 2 > n:
    high = mid - 1
  elif mid ** 2 < n:
    low = mid + 1