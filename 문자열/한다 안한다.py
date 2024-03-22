import sys

T = int(sys.stdin.readline())

for i in range(T):
  string = sys.stdin.readline().strip()

  if string[int(len(string)//2)] == string[int(len(string)//2)-1]:
    print('Do-it')
  else:
    print('Do-it-Not')