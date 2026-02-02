input = [4, 6, 2, 9, 1]


# 시간 복잡도: O(N^2)
def selection_sort(array):
    # 1번 코드
    for count in range(len(array)-1):
        max_number_index = 0
        for i in range(1, len(array)-count):
            if array[max_number_index] < array[i]:
                max_number_index = i
        array[len(array)-1-count], array[max_number_index] = array[max_number_index], array[len(array) - 1- count]

    # 2번 코드
    n = len(array)
    for i in range(n-1):
        min_index = i
        for j in range(n-i):
            if array[i+j] < array[min_index]:
                min_index = i+j
        array[i], array[min_index] = array[min_index], array[i]
    return array

# [1, 4, 2, 6]
# 총 3번
# 0
# 3번 비교해서 6을 맨 뒤로 보냄
# 1
# 2번 비교해서 4를 맨 뒤로 보냄
# 2
# 1번 비교해서 맨 뒤로 보냄

selection_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!

print("정답 = [1, 2, 4, 6, 9] / 현재 풀이 값 = ",selection_sort([4, 6, 2, 9, 1]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",selection_sort([3,-1,17,9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",selection_sort([100,56,-3,32,44]))