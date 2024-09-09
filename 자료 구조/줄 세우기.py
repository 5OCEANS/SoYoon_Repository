import sys

num = int(sys.stdin.readline())
studentList = list(map(int, sys.stdin.readline().strip().split()))

resultList = []

for i in range(num):
  resultList.insert(studentList[i], str(i+1))

resultList.reverse()

print(' '.join(resultList))