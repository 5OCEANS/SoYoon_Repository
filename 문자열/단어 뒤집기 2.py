import sys

S = sys.stdin.readline().strip()

index = 0

newString = ''

while index < len(S):
  if S[index] == '<':
    start = index
    while index < len(S) and S[index] != '>':
      index += 1
    newString += S[start:index+1]
    index += 1
  else:
    start = index
    while index < len(S) and S[index] != '<':
      index += 1
    tmpStringList = list(S[start:index].split())
    for i in range(len(tmpStringList)-1):
      newString += (tmpStringList[i][::-1] + ' ')
    newString += tmpStringList[-1][::-1]

print(newString)
    
    