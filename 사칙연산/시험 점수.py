import sys

minguk = sum(list(map(int, sys.stdin.readline().strip().split())))
mansae = sum(list(map(int, sys.stdin.readline().strip().split())))

print(max(minguk, mansae))