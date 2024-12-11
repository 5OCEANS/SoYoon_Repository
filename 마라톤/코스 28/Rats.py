import sys, math

numList = list(map(int, sys.stdin.readline().strip().split()))

print(math.floor((numList[0]+1)*(numList[1]+1)/(numList[2]+1)-1))