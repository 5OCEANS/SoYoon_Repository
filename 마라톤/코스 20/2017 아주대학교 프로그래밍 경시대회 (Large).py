import sys

N = int(sys.stdin.readline().strip())
peopleList = list()

for i in range(N):
  s, c, l = map(int, sys.stdin.readline().strip().split())
  peopleList.append((s, c, l))

sortedPeopleList = sorted(peopleList, key= lambda x:(-x[0], x[1], x[2]))

index = peopleList.index(sortedPeopleList[0])
print(index+1)