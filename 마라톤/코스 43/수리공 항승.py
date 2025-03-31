import sys

N, L = map(int, sys.stdin.readline().strip().split())
datas = [int(x) for x in sys.stdin.readline().strip().split()]
datas.sort()

L -= 1
now_d = datas[0]
count = 1
for d in datas[1:]:
  if (d - now_d) > L:
    now_d = d
    count += 1
      
print(count)