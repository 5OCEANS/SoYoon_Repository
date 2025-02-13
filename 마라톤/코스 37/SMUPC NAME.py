import sys

N, string = sys.stdin.readline().strip().split()
N = int(N)
chrList = list()
newString = ''
num = 0
for i in string:
  if i not in chrList:
    newString += i
    chrList.append(i)
    continue
  else:
    num += 1
string = str(N+1906) + newString + str(num+4)
print('smupc_' + string[::-1])