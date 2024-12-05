import sys

day = int(sys.stdin.readline())
carList = list(map(int, sys.stdin.readline().strip().split()))
print(carList.count(day))