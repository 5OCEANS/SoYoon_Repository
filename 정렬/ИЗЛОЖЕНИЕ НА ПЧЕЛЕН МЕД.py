import sys

priceList = list(map(int, sys.stdin.readline().strip().split()))
volumeList = list(map(int, sys.stdin.readline().strip().split()))
priceList.sort()
volumeList.sort()
print(priceList[0]*volumeList[0]+priceList[1]*volumeList[1]+priceList[2]*volumeList[2])