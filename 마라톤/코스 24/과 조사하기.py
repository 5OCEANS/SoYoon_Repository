import sys
from collections import defaultdict

P = int(sys.stdin.readline())
studentDic = defaultdict(int) # 1: 소프트웨어개발과 학생 2: 임베디드소프트웨어개발과 학생 3: 인공지능소프트웨어개발과 학생 4: 1학년

for i in range(P):
  g, c, n = map(int, sys.stdin.readline().strip().split())
  if g == 1:
    studentDic[4] += 1
  elif c == 1 or c == 2:
    studentDic[1] += 1
  elif c == 3:
    studentDic[2] += 1
  elif c == 4:
    studentDic[3] += 1

for i in range(1, 5):
  print(studentDic[i])