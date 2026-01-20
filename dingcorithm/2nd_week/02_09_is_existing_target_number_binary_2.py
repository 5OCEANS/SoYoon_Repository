finding_target = 2
finding_numbers = [0, 3, 5, 6, 1, 2, 4]

def is_exist_target_number_binary(target, array):
    left = 0
    right = len(array) - 1
    sorted_array = sorted(array)
    while left <= right:
        mid = (left + right) // 2
        if sorted_array[mid] == target:
            return True
        elif sorted_array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False


result = is_exist_target_number_binary(finding_target, finding_numbers)
print(result)