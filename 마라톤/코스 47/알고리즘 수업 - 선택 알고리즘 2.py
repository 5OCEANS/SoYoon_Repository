import sys
input = sys.stdin.readline

N, Q, K = map(int, input().split())
A = list(map(int, input().split()))
count = 0
found = False

def partition(p, r):
  global count, found
  x = A[r]
  i = p - 1
  for j in range(p, r):
    if A[j] <= x:
      i += 1
      A[i], A[j] = A[j], A[i]
      count += 1
      if count == K:
        print(' '.join(map(str, A)))
        found = True
        return -1
  if i + 1 != r:
    A[i + 1], A[r] = A[r], A[i + 1]
    count += 1
    if count == K:
      print(' '.join(map(str, A)))
      found = True
      return -1
  return i + 1

def quick_select(p, r, q):
  global found
  while p <= r:
    t = partition(p, r)
    if found or t == -1:
      return
    k = t - p + 1
    if q < k:
      r = t - 1
    elif q > k:
      q -= k
      p = t + 1
    else:
      return

quick_select(0, N - 1, Q)
if not found:
  print(-1)