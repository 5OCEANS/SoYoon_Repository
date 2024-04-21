import sys

N = int(sys.stdin.readline())

for i in range(N):
  nickname = sys.stdin.readline().strip().split()
  nickname[0] = 'god'

  for j in nickname:
    print(j, end ='')

  print()