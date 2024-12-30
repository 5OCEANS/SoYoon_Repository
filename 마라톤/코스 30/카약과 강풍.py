import sys

N, S, R = map(int, sys.stdin.readline().strip().split())
brokenNumList = set(map(int, sys.stdin.readline().strip().split()))
twoNumList = set(map(int, sys.stdin.readline().strip().split()))

answer = 0

intersection = brokenNumList & twoNumList
brokenNumList = list(brokenNumList - intersection)
twoNumList = list(twoNumList - intersection)

if not brokenNumList:
  answer = 0
else:
  brokenNumList.sort()

  for t in brokenNumList:
    if t-1 in twoNumList:
      twoNumList.remove(t-1)
    elif t+1 in twoNumList:
      twoNumList.remove(t+1)
    else:
      answer += 1

print(answer)