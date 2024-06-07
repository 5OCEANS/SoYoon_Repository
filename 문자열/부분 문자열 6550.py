import sys

strings = sys.stdin.readlines()

for string in strings:
  s, t = string.strip().split()

  num = 0

  for i in range(len(t)):
    if s[num] == t[i]:
      num += 1
    
    if num == len(s):
      print('Yes')
      break
  else:
    print('No')