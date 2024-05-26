import sys

N = int(sys.stdin.readline())

alpKey = {}

for i in range(N):
  val, alp = sys.stdin.readline().strip().split()

  alpKey[alp] = val

string = sys.stdin.readline().strip()
start, end = map(int, sys.stdin.readline().split())
resultString = ''

for i in range(len(string)):
  resultString += alpKey[string[i]]

print(resultString[start-1:end])