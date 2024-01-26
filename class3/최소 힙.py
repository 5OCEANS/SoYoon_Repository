# heapq 모듈 사용

import sys
import heapq

numbers = int(input())
heap = []

# Max heap
for i in range(numbers):
  num = int(sys.stdin.readline())
  if num != 0:
    heapq.heappush(heap, num)
  else:
    try:
      print(heapq.heappop(heap))
    except:
      print(0)