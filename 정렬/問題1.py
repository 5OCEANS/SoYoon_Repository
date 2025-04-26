import sys

n, m = map(int, sys.stdin.readline().strip().split())
placeDic = dict()
mList = list(map(int, sys.stdin.readline().strip().split()))
for j in range(m):
  placeDic[j+1] = mList[j]
for i in range(n-1):
  mList = list(map(int, sys.stdin.readline().strip().split()))
  for j in range(m):
    placeDic[j+1] += mList[j]
placeDic = dict(sorted(placeDic.items(), key= lambda x: (-x[1], x[0])))
for k, v in placeDic.items():
  print(k, end = " ")
print()


# 리팩토링
import sys

n, m = map(int, sys.stdin.readline().split())
place_count = [0] * m

for _ in range(n):
  votes = list(map(int, sys.stdin.readline().split()))
  for i in range(m):
    place_count[i] += votes[i]

places = [(i + 1, count) for i, count in enumerate(place_count)]

places.sort(key=lambda x: (-x[1], x[0]))

print(' '.join(str(place) for place, _ in places))