import sys

N = int(sys.stdin.readline().strip())

numList = []
alphabetList = 'abcdefghijklmnopqrstuvwxyz'

for i in range(N):
  string = sys.stdin.readline().strip()

  for j in range(len(alphabetList)):
    string = string.replace(alphabetList[j], ' ')
  
  stringNumList = map(int, string.strip().split())

  numList += stringNumList

numList.sort()

for i in range(len(numList)):
  print(numList[i])