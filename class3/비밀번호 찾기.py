import sys
n, m = map(int, sys.stdin.readline().strip().split())
siteList = {}

for i in range(n):
  add, passwrd = sys.stdin.readline().split()
  siteList[add] = passwrd

for i in range(m):
  add = sys.stdin.readline().strip()
  print(siteList.get(add))