import sys

P = int(sys.stdin.readline())
for _ in range(P):
  arr = list(map(int, sys.stdin.readline().strip().split()))
  total = 0
  for i in range(1, len(arr) - 1):
    for j in range(i+1, len(arr)): # i 뒤에 숫자들과 전부 비교해서
      if arr[i] > arr[j]: # i가 더 크면
        arr[i], arr[j] = arr[j], arr[i] # 교환
        total += 1
  print(arr[0], total)
