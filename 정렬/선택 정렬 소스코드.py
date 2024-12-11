array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(10):
  min_index = i
  for j in range(i+1, 10):
    if array[min_index] > array[j]:
      min_index = j
  array[i], array[min_index] = array[min_index], array[i] # 스와프

print(array)