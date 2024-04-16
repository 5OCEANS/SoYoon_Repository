import sys

N = int(sys.stdin.readline())

for i in range(N):
  string = sys.stdin.readline().strip()

  if string == 'P=NP':
    print('skipped')
  else:
    a, b = map(int, string.split('+'))
    print(a+b)