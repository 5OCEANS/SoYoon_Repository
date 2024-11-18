import sys

N = int(sys.stdin.readline())
result = 0

for i in range(1, N+1):
  digitSum = 0
  tmp = i
  while tmp:
    digitSum += tmp % 10
    tmp //= 10
  if i % digitSum == 0:
    result += 1

print(result)