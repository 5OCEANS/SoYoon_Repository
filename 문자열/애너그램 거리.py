import sys

N = int(sys.stdin.readline())

for i in range(N):
  str1 = sys.stdin.readline().strip()
  str2 = list(sys.stdin.readline().strip())

  cnt = 0

  for j in range(len(str1)):
    if str1[j] in str2:
      str2.pop(str2.index(str1[j]))
      continue
    else:
      cnt += 1
  
  cnt += len(str2)

  print('Case #%d: %d' %(i+1, cnt))