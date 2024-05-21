# 메모리 초과
import sys

S = sys.stdin.readline().strip()
suffixList = []

for i in range(len(S)):
  suffixList.append(S[0:i+1])

suffixList.sort()

for i in range(len(S)):
  print(len(suffixList[i])-1)

# 성공
s=input()
for i in range(len(s)):
  print(i)