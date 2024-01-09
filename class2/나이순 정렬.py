n = int(input())

pList = [] # pList[x][0] = 나이, pList[x][1] = 이름

for i in range(n):
  pList.append([])
  age, name = input().split()
  pList[i].extend([int(age), name])

pList.sort(key= lambda x: x[0]) # x가 리스트의 인덱스를 나타냄

for i in range(n):
  print(pList[i][0], pList[i][1])