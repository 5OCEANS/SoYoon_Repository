import sys

n, m = map(int, sys.stdin.readline().strip().split())
k = sorted(set(list(map(int, sys.stdin.readline().strip().split()))))
ans = []
p = []
def solve(depth, idx):
  if depth == m:
    print(' '.join(map(str, ans)))
    return

  for i in range(idx, len(k)):
    ans.append(k[i])
    solve(depth+1, i)
    ans.pop()

solve(0, 0)