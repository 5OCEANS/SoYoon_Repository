import sys

N = int(sys.stdin.readline())

for i in range(N):
  string = sys.stdin.readline().strip()

  sum = 0

  for j in string:
    if j.isalpha():
      sum += ord(j) - 64
  
  if sum == 100:
    print('PERFECT LIFE')
  else:
    print(sum)