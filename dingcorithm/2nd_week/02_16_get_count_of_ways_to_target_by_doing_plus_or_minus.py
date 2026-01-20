numbers = [1, 1, 1, 1, 1]
target_number = 3


def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target):
    # 1번 코드
    result = 0

    def dfs(index, num):
        nonlocal result
        if index == len(array):
            if num == target:
                result += 1
            return
        dfs(index+1, num + array[index])
        dfs(index+1, num - array[index])
        return

    dfs(0, 0)

    return result

    # 2번 코드
    def dfs(index, num):
        if index == len(array):
            return 1 if num == target else 0

        return (dfs(index+1, num+array[index]) + dfs(index+1, num-array[index]))
    return dfs(0, 0)

    # 3번 코드
    all_ways = []

    def get_all_ways_by_doing_plus_or_minus(array, current_index, current_sum):
        if current_index == len(array):
            all_ways.append(current_sum)
            return

        get_all_ways_by_doing_plus_or_minus(array, current_index + 1, current_sum + array[current_index])
        get_all_ways_by_doing_plus_or_minus(array, current_index + 1, current_sum - array[current_index])

    get_all_ways_by_doing_plus_or_minus(array, 0, 0)

    target_count = 0

    for way in all_ways:
        if way == target:
            target_count += 1

    return target_count


print(get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number))  # 5를 반환해야 합니다!