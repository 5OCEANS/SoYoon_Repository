# 런타임 에러
# n = int(input())
# numList = []
# popNum = round(n*0.15)

# for i in range(n):
#   num = int(input())
#   numList.append(num)

# numList.sort()

# for i in range(popNum):
#   numList.pop() # 뒤에서부터 삭제
#   del numList[0] # 앞에서부터 삭제

# print(round(sum(numList)/len(numList)))

# 입력 방식을 바꾸고 round()를 사용하지 않고 사사오입 방식의 사용자정의함수를 만듦
import sys

def round45(num):
  return int(num) + 1 if num - int(num) >= 0.5 else int(num)

n = int(sys.stdin.readline())
if n:
  numList = []
  popNum = round45(n*0.15)

  for i in range(n):
    num = int(sys.stdin.readline())
    numList.append(num)

  numList.sort()

  print(round45(sum(numList[popNum:-popNum] if popNum else numList)/(n-popNum*2)))
else:
  print(0)