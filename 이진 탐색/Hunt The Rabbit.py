import sys

def binary_search(array, target, start, end):
  while start <= end:
    mid = (start+end)//2
    if target > array[mid]:
      print(array[mid], end = ' ')
      start = mid + 1
    elif target < array[mid]:
      print(array[mid], end = ' ')
      end = mid - 1
    else:
      print(target)
      return True

numList = [i for i in range(1, 51)]

while True:
  try:
    num = int(sys.stdin.readline())
    if num == 0:
      break
    binary_search(numList, num, 0, len(numList)-1)
  except:
    break