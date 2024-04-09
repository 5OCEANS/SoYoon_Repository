import sys

N = int(sys.stdin.readline())

for i in range(N):
  string = sys.stdin.readline().strip()
  stringList = sys.stdin.readline().strip()

  cryptoquoteString = ''

  for j in string:
    if j.isspace():
      cryptoquoteString += ' '
    else:
      cryptoquoteString += stringList[ord(j)-65]
  
  print(cryptoquoteString)