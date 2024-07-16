import sys

N = int(sys.stdin.readline().strip())

numList = list(map(int, sys.stdin.readline().strip().split()))

ans = max(numList) - min(numList)

print(ans)