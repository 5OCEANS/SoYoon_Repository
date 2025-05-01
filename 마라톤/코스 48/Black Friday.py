import sys
from collections import Counter

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

count = Counter(a)
unique = [num for num in a if count[num] == 1]

if not unique:
  print("none")
else:
  max_unique = max(unique)
  print(a.index(max_unique) + 1)