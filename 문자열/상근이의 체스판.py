import sys

R, C = map(int, sys.stdin.readline().split())

A, B = map(int, sys.stdin.readline().split())

for j in range(R): # 행 4
  for k in range(A): # 행의 높이 3
    string = ''
    for i in range(C): # 열 2
      # for p in range(B): # 열의 너비 1 가장 tap이 많음
      if j % 2 == 0:
        if i % 2 == 0:
          string += 'X' * B
        else:
          string += '.' * B
      else:
        if i % 2 == 0:
          string += '.' * B
        else:
          string += 'X' * B
    print(string) 