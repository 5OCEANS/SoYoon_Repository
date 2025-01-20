import sys

n,m = map(int,sys.stdin.readline().strip().split())
n_class = [[] for i in range(n+1)]
while 1:
  c,p = map(str,sys.stdin.readline().split())
  if c == '0' and p == '0':
    break
  c = int(c)
  if len(n_class[c]) < m:
    n_class[c].append(p)
for i in range(1,n+1):
  n_class[i].sort()
  n_class[i].sort(key=lambda x:len(x))
for i in range(1,n+1):
  if i%2:
    for j in range(len(n_class[i])):
      print(i,n_class[i][j])
  else:
    continue
for i in range(1,n+1):
  if not i%2:
    for j in range(len(n_class[i])):
      print(i,n_class[i][j])
  else:
    continue