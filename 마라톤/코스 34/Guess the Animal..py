import sys
from collections import defaultdict

def max_common_characters(n, data):
  c = defaultdict(list)
  
  for i in range(n):
    name, k, *characters = data[i]
    c[i] = characters
  
  ans = 0
  for i in range(n):
    for j in range(i + 1, n):
      cnt = len(set(c[i]) & set(c[j])) # 공통 특성 개수 계산
      ans = max(ans, cnt)
  
  return ans + 1 # 최대 공통 특성 개수 + 1 마지막 yes를 받은 후 정답을 맞힐 수 있기 때문이다.

n = int(sys.stdin.readline().strip())
data = [sys.stdin.readline().split() for _ in range(n)]

data = [(d[0], int(d[1]), *d[2:]) for d in data]

print(max_common_characters(n, data))