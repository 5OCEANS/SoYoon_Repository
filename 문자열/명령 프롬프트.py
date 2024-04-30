import sys

N = int(sys.stdin.readline())

result = []

string = sys.stdin.readline().strip()

result = list(string)

for i in range(N-1):
  string = sys.stdin.readline().strip()

  for j in range(len(string)):
    if string[j] != result[j]:
      result[j] = '?'

print(''.join(result))