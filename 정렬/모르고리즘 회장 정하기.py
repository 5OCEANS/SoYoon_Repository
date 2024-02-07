import sys

N = int(sys.stdin.readline().strip())
pList = []

for i in range(N):
  person = sys.stdin.readline().strip()

  if len(person) == 3:
    pList.append(person)

pList.sort()

print(pList[0])  