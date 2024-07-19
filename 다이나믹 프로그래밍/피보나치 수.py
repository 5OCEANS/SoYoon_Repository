# 시간 초과
import sys

def fibonacci(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    n = fibonacci(n-1) + fibonacci(n-2)
    return n

n = int(sys.stdin.readline().strip())

print(fibonacci(n))


# 반복문
import sys

n = int(sys.stdin.readline())
a, b = 0, 1

for i in range(n):
  a, b = b, a + b

print(a)


# DP(다이나믹 프로그래밍)
import sys

n = int(sys.stdin.readline())
d = [0] * (n+1)

if n == 1:
  d[1] = 1
  print(d[1])
elif n == 2:
  d[2] = 1
  print(d[2])
else:
  d[1] = 1
  d[2] = 1

  for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2] 
  
  print(d[n])