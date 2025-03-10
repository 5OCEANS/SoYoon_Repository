import sys

def count(li, m, N):
  t = 0
  for i in range(N):
    for j in range(N):
      t += (m if m <= li[i][j] else li[i][j])
  return t

N = int(input())
li = []
max_li = sum_li = 0
for _ in range(N):
  a = list(map(int, sys.stdin.readline().strip().split()))
  li.append(a)
  max_li = max(max_li, max(a))
  sum_li += sum(a)
s, e = 0, max_li
res = 0
while s <= e:
  m = (s+e)//2
  if count(li, m, N) >= sum_li/2:
    res = m
    e = m-1
  else:
    s = m+1
print(res)