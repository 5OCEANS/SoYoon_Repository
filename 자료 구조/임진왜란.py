# 시간 초과
import sys

N = int(sys.stdin.readline())

battleList = list(sys.stdin.readline().strip().split())
answer = list(sys.stdin.readline().strip().split())
b = int(N*(N-1) / 2)
a = 0

for i in range(N):
  answerFirstIndex = answer.index(battleList[i])
  for j in range(i+1, N):
    answerSecondIndex = answer.index(battleList[j])
    if answerFirstIndex < answerSecondIndex:
      a += 1

print(str(a)+'/'+str(b))

# 성공
import sys

N = int(sys.stdin.readline())
battleList = list(sys.stdin.readline().strip().split())
answer = list(sys.stdin.readline().strip().split())

answer_index = {answer[i]: i for i in range(N)}
b = int(N*(N-1)/2)
a = 0

for i in range(N):
  for j in range(i+1, N):
    if answer_index[battleList[i]] < answer_index[battleList[j]]:
      a += 1

print(str(a)+'/'+str(b))