input = 20

def find_prime_list_under_number(number):
    # 첫 번째 방법
    answer = list()
    for num in range(2, number+1):
        for small_num in range(2, num):
            if num % small_num == 0:
                break
        else:
            answer.append(num)

    return answer

    # 두 번째 방법
    answer = list()
    for num in range(2, number+1):
        # n보다 작은 모든 소수에 대해 검사(answer)
        for small_num in answer:
            if num % small_num == 0:
                break
        else:
            answer.append(num)
    return answer

    # 세 번째 방법 - N의 제곱근보다 크지 않은 어떤 소수로도 나누어 떨어지지 않는다.
    answer = list()
    for num in range(2, number+1):
        for small_num in answer:
            if small_num * small_num <= num and num % small_num == 0:
                break
        else:
            answer.append(num)
    return answer


result = find_prime_list_under_number(input)
print(result)