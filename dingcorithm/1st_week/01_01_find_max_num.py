def find_max_num(array):
    # 첫 번째 방법
    max_num = 0
    for num in array:
        if num > max_num:
            max_num = num
    return max_num
    # 두 번째 방법
    return max(array)


print("정답 = 6 / 현재 풀이 값 = ", find_max_num([3, 5, 6, 1, 2, 4]))
print("정답 = 6 / 현재 풀이 값 = ", find_max_num([6, 6, 6]))
print("정답 = 1888 / 현재 풀이 값 = ", find_max_num([6, 9, 2, 7, 1888]))