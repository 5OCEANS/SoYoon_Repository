import sys

stones = list(sys.stdin.readline().strip())
print(1 if stones.count('B') == stones.count('W') else 0)