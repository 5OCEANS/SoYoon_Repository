import sys

N, M = map(int, sys.stdin.readline().split())
painting = []

for i in range(N):
  string = list(sys.stdin.readline().strip())

  for j in range(M//2):
    if string[j] != '.':
      string[M-1-j] = string[j]
    elif string[j] == '.' and string[M-1-j] != '.':
      string[j] = string[M-1-j]
  painting.append(''.join(string))

for i in range(N):
  print(painting[i])

# 변수 사용 X
import sys

N, M = map(int, sys.stdin.readline().split())

for i in range(N):
  string = list(sys.stdin.readline().strip())

  for j in range(M//2):
    if string[j] != '.':
      string[M-1-j] = string[j]
    elif string[j] == '.' and string[M-1-j] != '.':
      string[j] = string[M-1-j]
  print(''.join(string))
