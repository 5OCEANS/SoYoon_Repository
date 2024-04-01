import sys

N = int(sys.stdin.readline())

st = sys.stdin.readline().strip()

for i in range(N):
  st2 = st[i:N]

  if st2.count('s') == st2.count('t'):
    print(st2)
    break