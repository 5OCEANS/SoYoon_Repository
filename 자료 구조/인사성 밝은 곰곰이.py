# 시간 초과 -> list에 대해 중복 확인을 위한 in 연산이 O(N)의 시간 복잡도를 가짐. 그래서 시간 초과
import sys

N = int(sys.stdin.readline())
namelist = []
count = 0

for i in range(N):
  chat = sys.stdin.readline().strip()
  if chat == 'ENTER':
    namelist = []
  else:
    if chat in namelist:
      continue
    else:
      count += 1
      namelist.append(chat)

print(count)


# set 사용 -> set은 중복된 요소를 허용하지 않으며, in 연산자는 O(1)의 시간복잡도를 가지기 때문에 성능이 개선됨.
import sys

N = int(sys.stdin.readline())
nameset = set()
count = 0

for i in range(N):
  chat = sys.stdin.readline().strip()

  if chat == 'ENTER':
    nameset = set()
  else:
    if chat in nameset:
      continue
    else:
      nameset.add(chat)
      count += 1

print(count)
