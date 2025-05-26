import sys
from collections import defaultdict

def max_continuous_length(N, K, A):
  pos = defaultdict(list)

  for idx, num in enumerate(A):
    pos[num].append(idx)

  max_len = 0
  for indices in pos.values():
    left = 0

    for right in range(len(indices)):
      needed_deletion = indices[right] - indices[left] - (right - left)
      while needed_deletion > K:
        left += 1
        needed_deletion = indices[right] - indices[left] - (right - left)
      max_len = max(max_len, right - left + 1)

  return max_len

N, K = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

print(max_continuous_length(N, K, A))