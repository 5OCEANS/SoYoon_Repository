def is_number_exist(number, array):
    # 첫 번째 방법
    return True if number in array else False
    # 두 번째 방법
    for element in array:
        if number == element:
            return True
    return False


result = is_number_exist
print("정답 = True 현재 풀이 값 =", result(3, [3,5,6,1,2,4]))
print("정답 = False 현재 풀이 값 =", result(7, [6,6,6]))
print("정답 = True 현재 풀이 값 =", result(2, [6,9,2,7,1888]))