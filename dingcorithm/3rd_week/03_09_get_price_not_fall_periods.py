prices = [1, 2, 3, 2, 3]


def get_price_not_fall_periods(prices):
    from collections import deque
    prices = deque(prices)
    answer = [0]*len(prices)

    for i in range(len(prices)):
        price = prices.popleft()
        price_not_fall_period = 0
        for compare_price in prices:
            price_not_fall_period += 1
            if price > compare_price:
                break
        answer[i] = price_not_fall_period
    return answer


print(get_price_not_fall_periods(prices))

print("정답 = [4, 3, 1, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods(prices))
print("정답 = [6, 2, 1, 3, 2, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods([3, 9, 9, 3, 5, 7, 2]))
print("정답 = [6, 1, 4, 3, 1, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods([1, 5, 3, 6, 7, 6, 5]))