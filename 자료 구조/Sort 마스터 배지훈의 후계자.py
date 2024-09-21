# 시간 초과
import sys

N, M = map(int, sys.stdin.readline().strip().split())
a = []
b = []

for i in range(N):
  num = int(sys.stdin.readline())
  a.append(num)

b = sorted(a)

for i in range(M):
  num = int(sys.stdin.readline())

  if num not in b:
    print(-1)
    continue  

  print(b.index(num))

# 성공 딕셔너리 사용
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

alist = sorted([int(input()) for _ in range(n)])

aidx = dict()
for i in range(n):
  if alist[i] not in aidx:
    aidx[alist[i]] = i

for i in range(m):
  d = int(input())
  print(aidx[d] if d in aidx else -1)