import sys

N = int(sys.stdin.readline())
stringList = list(sys.stdin.readline().strip().split())
ans = stringList.count('he') + stringList.count('him') + stringList.count('she') + stringList.count('her')
print(ans)