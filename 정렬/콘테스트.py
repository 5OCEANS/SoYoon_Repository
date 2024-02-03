import sys

Wlist = []
Klist = []

Wscore = 0
Kscroe = 0

for i in range(10):
  num = int(sys.stdin.readline())
  Wlist.append(num)

Wlist.sort(reverse=True)
Wscore = sum(Wlist[0:3])

for i in range(10):
  num = int(sys.stdin.readline())
  Klist.append(num)

Klist.sort(reverse=True)
Kscore = sum(Klist[0:3])

print(Wscore, Kscore)