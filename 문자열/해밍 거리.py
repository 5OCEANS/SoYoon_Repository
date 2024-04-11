import sys

T = int(sys.stdin.readline())

for i in range(T):
  str1 = sys.stdin.readline().strip()
  str2 = sys.stdin.readline().strip()

  cnt = 0

  for j in range(len(str1)):
    if str1[j] == str2[j]:
      continue
    else:
      cnt += 1
  
  print('Hamming distance is %d.' % (cnt))