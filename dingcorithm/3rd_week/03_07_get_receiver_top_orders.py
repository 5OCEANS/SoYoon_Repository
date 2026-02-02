top_heights = [6, 9, 5, 7, 4]


def get_receiver_top_orders(heights):
    # 스택 이용 X
    def is_touched(standard, height):
        if standard < height:
            return False
        return True

    length = len(heights)
    answer = [0] * length

    for i in range(length-1, 0, -1):
        for j in range(i-1, -1, -1):
            if is_touched(heights[j], heights[i]):
                answer[i] = j+1
                break

    # 스택 이용 O
    def is_touched(standard, height):
        if standard < height:
            return False
        return True

    length = len(heights)
    answer = [0] * length

    while heights:
        height = heights.pop()
        for i in range(len(heights)-1, -1, -1):
            if is_touched(heights[i], height):
                answer[len(heights)] = i+1
                break

    # 시간 복잡도 O(N)
    answer = [0] * len(heights)
    stack = []

    for idx, h in enumerate(heights, start=1):
        # 현재 탑보다 낮은 탑은 수신자가 될 수 없으니 제거
        while stack and stack[-1][1] < h:
            stack.pop()

        # 남아있는 top이 "가장 가까운 높거나 같은 탑"
        answer[idx - 1] = stack[-1][0] if stack else 0

        # 현재 탑을 후보로 넣기
        stack.append((idx, h))

    return answer


print(get_receiver_top_orders(top_heights))  # [0, 0, 2, 2, 4] 가 반환되어야 한다!

print("정답 = [0, 0, 2, 2, 4] / 현재 풀이 값 = ", get_receiver_top_orders([6,9,5,7,4]))
print("정답 = [0, 0, 2, 3, 3, 3, 6] / 현재 풀이 값 = ", get_receiver_top_orders([3,9,9,3,5,7,2]))
print("정답 = [0, 0, 2, 0, 0, 5, 6] / 현재 풀이 값 = ", get_receiver_top_orders([1,5,3,6,7,6,5]))