import sys

K = int(sys.stdin.readline())

S = sys.stdin.readline().strip()

num = len(S)

cnt = 0

while cnt < num:
  print(S[cnt], end ='')
  cnt += K