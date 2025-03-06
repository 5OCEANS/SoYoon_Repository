import sys

n = int(sys.stdin.readline().strip())
computerdic = dict()
for i in range(n):
  name, ram, cpu, disk = sys.stdin.readline().strip().split()
  preference = 2*int(ram)+3*int(cpu)+int(disk)
  computerdic[name] = preference
computerdic = dict(sorted(computerdic.items(), key= lambda x:(-x[1], x[0])))
if len(computerdic) == 1:
  for i in list(computerdic.keys()):
    print(i)
else:
  for i in list(computerdic.keys())[:2]:
    print(i)