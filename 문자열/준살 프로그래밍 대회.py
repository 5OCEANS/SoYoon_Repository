import sys

T = int(sys.stdin.readline())

for i in range(T):
  print('Scenario #%d:' % (i + 1))
  m = int(sys.stdin.readline())

  wordList = []
  passwordList = []

  for j in range(m):
    word = sys.stdin.readline().strip()
    wordList.append(word)

  n = int(sys.stdin.readline())

  for j in range(n):
    passwordList = list(map(int, sys.stdin.readline().strip().split()))
    
    for k in range(passwordList[0]):
      print(wordList[passwordList[k+1]], end = '')
    print()
  
  print()