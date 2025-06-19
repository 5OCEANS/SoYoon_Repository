import sys

N = int(sys.stdin.readline().strip())
timeList = list(map(int, sys.stdin.readline().strip().split()))

spent = sum(timeList) + (len(timeList) - 1) * 8
print(spent//24, spent%24)