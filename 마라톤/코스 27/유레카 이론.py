import sys

numList = [(n*(n+1)//2) for n in range(1, 45)] # 45가 1035
ansSet = set()

for i in range(len(numList)): # 미리 삼각수인 경우 Set에 넣어둠
  for j in range(len(numList)):
    for k in range(len(numList)):
      num = numList[i] + numList[j] + numList[k]
      if num <= 1000:
        ansSet.add(num) # 삼각수인 경우 ansSet에 추가

t = int(sys.stdin.readline())
for _ in range(t):
  k = int(sys.stdin.readline())
  if k in ansSet:
    print(1)
  else:
    print(0)