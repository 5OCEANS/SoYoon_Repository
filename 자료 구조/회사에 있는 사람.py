import sys

peopleSet = set()

n = int(sys.stdin.readline())

for i in range(n):
  name, string = sys.stdin.readline().strip().split()

  if string == 'enter':
    peopleSet.add(name)
  elif string == 'leave':
    peopleSet.remove(name)

sortedPeopleSet = sorted(peopleSet, reverse=True)

for i in range(len(sortedPeopleSet)):
  print(sortedPeopleSet[i])