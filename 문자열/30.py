import sys

num = sys.stdin.readline().strip()

if sum(list(map(int, list(num)))) % 3 == 0:
  if '0' in list(num):
    index = num.index('0')
    tmpStr = num[0:index] + num[index+1:]
    tmpStrList = list(tmpStr)
    tmpStrList.sort(reverse=True)
    ans = ''.join(tmpStrList) + '0'
    print(ans)
  else:
    print(-1)
else:
  print(-1)