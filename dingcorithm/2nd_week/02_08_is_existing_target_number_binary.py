finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

# 시간 복잡도 -> O(log(N))
def is_existing_target_number_binary(target, array):
    find_count = 0
    left = 0
    right = len(array) - 1

    while left <= right:
        find_count += 1
        mid = (left + right) // 2
        if array[mid] == target:
            print(find_count)
            return mid
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)