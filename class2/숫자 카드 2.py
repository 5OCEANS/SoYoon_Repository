# 시간초과
n = int(input())

cardList = list(map(int, input().split()))

numCnt = int(input())

numList = list(map(int, input().split()))

for i in numList:
  num = cardList.count(i)
  print(num, end=' ')

# 런타임 에러: 메모리 사용이 과도하게 커짐. 주어진 제한 범위 내에서 배열을 할당하면서 발생하는 메모리 초과
import sys

n = int(sys.stdin.readline())

numList = [0] * 20000001

cardList = list(map(int, input().split()))
for i in range(n):
  numList[cardList[i]+10000001] += 1

findNumCnt = int(input())
findNumList = list(map(int, input().split()))

for i in findNumList:
  print(numList[i+10000001], end=' ')

# 딕셔너리 이용, 키 조회 key: 카드의 숫자, value: 그 카드의 개수
import sys

input = sys.stdin.readline

N = int(input())
cards = [*map(int, input().split())]
M = int(input())
candidate = [*map(int, input().split())]

count = {}
for card in cards:
  if card in count:
    count[card] += 1
  else:
    count[card] = 1

for target in candidate:
  result = count.get(target)
  if result == None:
    print(0, end=' ')
  else:
    print(result, end=' ')