# arr = [5, 4, 3, 2, 1]에서 누적합을 구해보자.
# S = [0, 5, 9, 12, 14, 15]로 누적합 리스트인 S를 구할 수 있다. (맨 처음 원소는 0으로 고정)

# ex1) 0 ~ 2(인덱스)범위의 구간 합을 구해보자.
# -> arr[0] + arr[1] + arr[2] = 5 + 4 + 3 = 12이다. 이렇게 하나씩 더할 필요없이 S[3] - S[0] = 12 - 0의 값을 
# 계산해주어 0 ~ 2 범위의 구간 합을 구할 수 있다.

# ex) 1 ~ 3 범위의 구간 합을 구해보자.
# -> arr[1] + arr[2] + arr[3]의 값을 구해주면 되는데, 위 예제처럼 리스트 S를 이용하여 풀면
# S[4] - S[1] = 14 - 5 = 9로 해당 구간 합을 구할 수 있게 된다.

# 즉, 문제에서 주어진 구간을 i, j라고 할 때, i부터 j까지의 구간 합을 S[j] - S[i-1]으로 표현할 수 있다.

# 누적 합으로 구간 합을 구하는 방법을 숙지해 둘 것.

import sys

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().strip().split()))

sum_list = [0]
total = 0

for i in range(len(arr)):
  total += arr[i]
  sum_list.append(total)

for _ in range(m):
  i, j = map(int, sys.stdin.readline().split())
  print(sum_list[j] - sum_list[i-1])