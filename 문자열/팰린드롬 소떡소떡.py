import sys

N = int(sys.stdin.readline())

string = sys.stdin.readline().strip()

newString = string[::-1]

cnt = 0

for i in range(len(string)//2):
  if string[i] != newString[i]:
    cnt += 1

print(cnt)