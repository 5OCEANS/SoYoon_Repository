# input()은 더이상 입력이 없는데도 수행될 경우 EOFerror를 발생시키는 반면, sys.stdin.readline()은 빈 문자열을 반환한다. 
# 후자를 사용할 경우, 무한 루프에서 빠져나오지 못해 시간 초과가 발생

stringList = ''

while True:
  try:
    string = input().strip()
    stringList += string
  except:
    break

numList = map(int, stringList.split(','))

print(sum(numList))

# 입력 데이터를 한 번에 읽은 후, 줄바꿈 문자를 제거하고 처리한다. 입력 데이터가 한 번에 주어진다고 가정한다.

import sys

data = sys.stdin.read()
data = data.replace('\n', '')
print(sum(map(int, data.split(','))))