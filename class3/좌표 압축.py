# 시간 초과

# import sys

# N = int(sys.stdin.readline())

# nlist = []
# sortNList = []

# nlist = list(map(int, sys.stdin.readline().strip().split()))

# sortNList = sorted(set(nlist))

# for i in range(N):
#   num = sortNList.index(nlist[i])
#   print(num, end= ' ')

# dict 사용
import sys

N = int(sys.stdin.readline())

nlist = []
sortNList = {}

nlist = list(map(int, sys.stdin.readline().strip().split()))

sortNList = sorted(set(nlist))
nDic = {sortNList[i] : i for i in range(len(sortNList))}

for i in range(N):
  num = nDic[nlist[i]]
  print(num, end= ' ')