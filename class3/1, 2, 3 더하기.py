# 4를 1과 2와 3으로 표현하는 방법은 7가지

# 5을 표현하는 방법
# 4에서 1을 더하는 방법
# 3에서 2를 더하는 방법
# 2에서 3을 더하는 방법

# 6을 표현하는 방법
# 5에서 1을 더하는 방법
# 4에서 2를 더하는 방법
# 3에서 3을 더하는 방법

# N을 표현하는 방법
# array[N] = array[N-1] + array[N-2] + array[N-3]

import sys

array = [0] * 12
array[1] = 1
array[2] = 2
array[3] = 4

for i in range(4, 11, 1):
  array[i] = array[i-3] + array[i-2] + array[i-1]

t = int(sys.stdin.readline())

for i in range(t):
  n = int(sys.stdin.readline())
  print(array[n])