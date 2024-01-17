# 시간 초과
import sys
n, m = map(int, sys.stdin.readline().split())
nlist = []
nmlist = []

for i in range(n):
  nlist.append(sys.stdin.readline().rstrip())

for i in range(m):
  person = sys.stdin.readline().rstrip()
  if person in nlist:
    nmlist.append(person)

nmlist.sort()

print(len(nmlist))
for i in nmlist:
  print(i)

# 딕셔너리 사용 성공
import sys
n, m = map(int, sys.stdin.readline().split())
nlist = {}
nmlist = []

for i in range(n):
  person = sys.stdin.readline().rstrip()
  nlist[person] = i

for i in range(m):
  person = sys.stdin.readline().rstrip()
  if person in nlist:
    nmlist.append(person)

nmlist.sort()

print(len(nmlist))
for i in nmlist:
  print(i)