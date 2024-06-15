# # 런타임 에러
# import sys

# N = int(sys.stdin.readline())
# timeDic = {}

# for i in range(N):
#   for j in range(4):
#     nameList = list(sys.stdin.readline().strip().split())
#     time = 0
#     if j % 2 == 0:
#       # 근무시간이 4시간임.
#       time = 4
#     elif j == 1:
#       # 근무시간이 6시간임.
#       time = 6
#     else:
#       # 근무 시간이 10시간임.
#       time = 10
    
#     for k in range(7):
#       if nameList[k] == '-':
#         continue
#       if nameList[k] in timeDic:
#         timeDic[nameList[k]] += time
#       else:
#         timeDic[nameList[k]] = time

# if max(list(timeDic.values())) - min(list(timeDic.values())) > 12:
#   print('No')
# else:
#   print('Yes')


import sys

N = int(sys.stdin.readline().strip())
timeDic = {}

for i in range(N):
  for j in range(4):
    nameList = sys.stdin.readline().strip().split()
    
    # 근무 시간을 결정
    if j % 2 == 0:
      time = 4
    elif j == 1:
      time = 6
    else:
      time = 10

    # 이름 리스트가 7명이 아닐 수 있는 경우를 대비해 처리
    for k in range(len(nameList)):
      if nameList[k] == '-':
        continue
      if nameList[k] in timeDic:
        timeDic[nameList[k]] += time
      else:
        timeDic[nameList[k]] = time

if not timeDic:
  print('Yes')
else:
  maxTime = max(timeDic.values())
  minTime = min(timeDic.values())
  
  if maxTime - minTime > 12:
    print('No')
  else:
    print('Yes')
