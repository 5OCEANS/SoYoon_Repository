a, b, v = map(int, input().split())

days = (v-b) / (a-b) # 낮에는 올라가고 밤에는 미끄러지므로, 올라가야하는 높이를 (a-b)로 나눠주면 됨. 정상에 올라가면 떨어지지 않기 때문에 낮에 다 올라가는 경우를 고려해 올라가야하는 높이를 (v-b)로 해줌.

print(int(days) if days == int(days) else int(days)+1)