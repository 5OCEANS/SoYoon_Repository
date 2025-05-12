import sys

n = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(n)]

arr.sort()

sum_level = 0
block = 0
start = n - 1
end = n - 42 if n > 42 else 0

for i in range(start, end - 1, -1):
  sum_level += arr[i]
  if arr[i] >= 250:
    block += 5
  elif arr[i] >= 200:
    block += 4
  elif arr[i] >= 140:
    block += 3
  elif arr[i] >= 100:
    block += 2
  elif arr[i] >= 60:
    block += 1

print(f"{sum_level} {block}")