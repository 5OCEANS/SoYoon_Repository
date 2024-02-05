import sys

N, k = map(int, sys.stdin.readline().strip().split())

scoreList =list(map(int, sys.stdin.readline().strip().split()))
            
scoreList.sort(reverse=True)

print(scoreList[k-1])