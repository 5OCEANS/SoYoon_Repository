import sys

nrows, ncolumns = map(int, sys.stdin.readline().strip().split())
nList = list()
cardinalcount = 0
intercardinalcount = 0
for i in range(ncolumns):
  rowList = list(map(int, sys.stdin.readline().strip().split()))
  nList.append(rowList)

for i in range(ncolumns):
  for j in range(nrows):
    if nList[i][j] == 1:
      if 0 <= i < ncolumns and 0 <= j+1 < nrows and nList[i][j+1] == 1:
        cardinalcount += 1
        intercardinalcount += 1
      if 0 <= i+1 < ncolumns and 0 <= j < nrows and nList[i+1][j] == 1:
        cardinalcount += 1
        intercardinalcount += 1
      if 0 <= i+1 < ncolumns and 0 <= j-1 < nrows and nList[i+1][j-1] == 1:
        intercardinalcount += 1
      if 0 <= i+1 < ncolumns and 0 <= j+1 < nrows and nList[i+1][j+1] == 1:
        intercardinalcount += 1
print(cardinalcount, intercardinalcount)