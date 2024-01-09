numCnt = int(input())

numList = set(map(int, input().split()))

findCnt = int(input())

findList = list(map(int, input().split()))

for i in range(findCnt):
  if findList[i] in numList: # 리스트에서의 in은 O(n)이고 세트에서의 in은 O(1)로 작동
    print(1)
  else:
    print(0)