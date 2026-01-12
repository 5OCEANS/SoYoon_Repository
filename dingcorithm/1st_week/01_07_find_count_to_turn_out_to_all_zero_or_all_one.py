input = "011110"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    # 첫 번째 방법
    # change_count = 0
    # now_num = string[0]
    # for i in string:
    #     if i != now_num:
    #         change_count += 1
    #         now_num = i
    # team_number = change_count + 1
    # answer = team_number // 2
    #
    # return answer

    # 두 번째 방법
    count_to_all_zero = 0
    count_to_all_one = 0

    if string[0] == '0':
        count_to_all_one += 1
    elif string[0] == '1':
        count_to_all_zero += 1

    for i in range(len(string) - 1):
        if string[i] != string[i+1]:
            if string[i+1] == '1':
                count_to_all_zero += 1
            if string[i+1] == '0':
                count_to_all_one += 1
    return min(count_to_all_zero, count_to_all_one)


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)
