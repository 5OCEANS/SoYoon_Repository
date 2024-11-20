import sys

N = int(sys.stdin.readline())

if N == 1:
  print('*')
else:
  evenString = '* ' * (N//2) + ('*' if N % 2 else '')
  oddString = ' *' * (N//2)
  for i in range(N*2):
    if i % 2 == 0:
      print(evenString.rstrip())
    else:
      print(oddString.rstrip())