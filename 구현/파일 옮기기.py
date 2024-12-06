import sys

firstA, firstB = map(int, sys.stdin.readline().strip().split())
secondA, secondB = map(int, sys.stdin.readline().strip().split())

print(min(firstA+secondB, secondA+firstB))