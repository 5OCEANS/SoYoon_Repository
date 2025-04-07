import sys
from itertools import product

def is_valid(s):
  count = 0
  for ch in s:
    if ch == '(':
      count += 1
    else:
      count -= 1
    if count < 0:
      return False
  return count == 0

N = int(sys.stdin.readline())
line = sys.stdin.readline().strip()

g_indices = [i for i, ch in enumerate(line) if ch == 'G']

for comb in product('()', repeat=len(g_indices)):
  chars = list(line)
  for idx, paren in zip(g_indices, comb):
    chars[idx] = paren
  candidate = ''.join(chars)
  if is_valid(candidate):
    print(candidate)
    break
