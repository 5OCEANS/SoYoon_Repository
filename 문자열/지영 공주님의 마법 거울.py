import sys

N = int(sys.stdin.readline())

stringList = []

for i in range(N):
  string = sys.stdin.readline().strip()
  stringList.append(string)

K = int(sys.stdin.readline())

if K == 1:
  for i in range(N):
    print(stringList[i])

elif K == 2:
  for i in range(N):
    print(stringList[i][::-1])
  
elif K == 3:
  for i in range(N):
    print(stringList[N-1-i])