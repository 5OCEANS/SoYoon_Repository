import sys
from collections import Counter

s = sys.stdin.readline().strip()
cnt = Counter(s)
kind = len(cnt)

if kind <= 2:
  print(0)
else:
  freq = sorted(cnt.values())
  erase = 0
  remove_kind = kind - 2 
  for i in range(remove_kind):
    erase += freq[i]  
  print(erase)