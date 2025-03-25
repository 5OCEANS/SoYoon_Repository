import sys

n = int(sys.stdin.readline())
canisters = list(map(int, sys.stdin.readline().split()))

canisters.sort()             
balloon_sizes = list(range(1, n + 1))

def is_possible(f):
  for i in range(n):
    if canisters[i] < f * balloon_sizes[i]:
      return False
  return True

lo, hi = 0.0, 1.0
eps = 1e-7

for i in range(n):
  if canisters[i] > balloon_sizes[i]:
    print("impossible")
    exit()

for _ in range(100):  
  mid = (lo + hi) / 2
  if is_possible(mid):
    lo = mid
  else:
    hi = mid

print(f"{lo:.10f}")