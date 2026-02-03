shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]


def get_max_discounted_price(prices, coupons):
    # 정렬 후 coupons 순서대로 적용
    from collections import deque

    prices.sort(reverse=True)
    prices_queue = deque(prices)
    coupons.sort(reverse=True)
    coupons_queue = deque(coupons)

    answer = 0

    while len(prices_queue) > 0 and len(coupons_queue) > 0:
        price = prices_queue.popleft()
        coupon = coupons_queue.popleft()
        answer += int(((100-coupon)/100) * price)

    answer += sum(prices_queue)

    return answer


print("정답 = 926000 / 현재 풀이 값 = ", get_max_discounted_price([30000, 2000, 1500000], [20, 40]))
print("정답 = 485000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], [10, 70, 30, 20]))
print("정답 = 1550000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], []))
print("정답 = 1458000 / 현재 풀이 값 = ", get_max_discounted_price([20000, 100000, 1500000], [10, 10, 10]))