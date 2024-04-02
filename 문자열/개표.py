import sys

N = int(sys.stdin.readline())

voteList = sys.stdin.readline().strip()

ACnt = voteList.count('A')
BCnt = voteList.count('B')

if ACnt > BCnt:
  print('A')
elif ACnt < BCnt:
  print('B')
elif ACnt == BCnt:
  print('Tie')