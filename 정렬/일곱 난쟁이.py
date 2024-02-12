# for문 이용

array = []
for i in range(9):
  array.append(int(input()))

array.sort()

sum_ = sum(array)

# 만약 모두 다 더하고 2명을 뺐을 때 그 값이 100이라면 2개를 뺀 나머지 값들을 출력
for i in range(len(array)):
  for j in range(i + 1, len(array)):
    if sum_ - array[i] - array[j] == 100:
      for k in range(len(array)):
        if k == i or k == j:
          pass
        else:
          print(array[k])
      exit()

# combinations 라이브러리 이용
import itertools

array = [int(input()) for _ in range(9)]

for i in itertools.combinations(array, 7): # 해당 배열을 7명 중복없이 뽑아준다.
  if sum(i) == 100: 
    for j in sorted(i):
      print(j)
    break

# 재귀 이용
short_men = [int(input()) for _ in range(9)]
seven_short_temp = []

def dfs(depth, start):
  if depth == 7:
    if sum(seven_short_temp) == 100:
      for j in sorted(seven_short_temp):
        print(j)
      exit()
    else:
      return
  
  for i in range(start, len(short_men)):
    seven_short_temp.append(short_men[i])
    dfs(depth + 1, i+1)
    seven_short_temp.pop()

dfs(0, 0)