# P 면적이 베개의 면적과 동일하다면 가희가 베개 위에서 자고 있지 않은 상태. 만약 다르다면 가희가 베개 위에서 자고 있는 상태이다.
import sys

R, C = map(int, sys.stdin.readline().split())

dogR, dogC, pillowR, pillowC = map(int, sys.stdin.readline().split())

MAP = [list(sys.stdin.readline().strip()) for i in range(R)]

cnt = 0
for i in range(R):
  for j in range(C):
    if MAP[i][j] == 'P':
      cnt += 1

if cnt == pillowR * pillowC:
  print(0)
else:
  print(1)

# count() 사용
import sys

R, C = map(int, sys.stdin.readline().split())

dogR, dogC, pillowR, pillowC = map(int, sys.stdin.readline().split())

MAP = [list(sys.stdin.readline().strip()) for i in range(R)]

cnt = 0
for i in range(R):
  cnt += MAP[i].count('P')

if cnt == pillowR * pillowC:
  print(0)
else:
  print(1)