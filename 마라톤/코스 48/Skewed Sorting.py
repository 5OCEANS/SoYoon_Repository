import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

N = int(input())
cows = [int(input()) for _ in range(2 ** N)]

total_distance = 0

def sort_and_count(arr, l, r):
  global total_distance
  if r - l <= 1:
    return

  mid = (l + r) // 2
  sort_and_count(arr, l, mid)
  sort_and_count(arr, mid, r)

  left = arr[l:mid]
  right = arr[mid:r]

  if right < left:
    arr[l:r] = right + left
    dist = (mid - l) * 2  
    total_distance += dist * (r - l) // 2

sort_and_count(cows, 0, len(cows))

print(total_distance)
for cow in cows:
  print(cow)