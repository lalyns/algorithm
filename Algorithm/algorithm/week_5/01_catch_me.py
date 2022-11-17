from collections import deque

#Q. 연인 코니와 브라운은 광활한 들판에서 ‘나 잡아 봐라’ 게임을 한다. 
# 이 게임은 브라운이 코니를 잡거나, 코니가 너무 멀리 달아나면 끝난다. 
# 게임이 끝나는데 걸리는 최소 시간을 구하시오.

# 조건은 다음과 같다.
# 코니는 처음 위치 C에서 1초 후 1만큼 움직이고, 
# 이후에는 가속이 붙어 매 초마다 이전 이동 거리 + 1만큼 움직인다. 
# 즉 시간에 따른 코니의 위치는 C, C + 1, C + 3, C + 6, …이다.

# 브라운은 현재 위치 B에서 다음 순간 B – 1, B + 1, 2 * B 중 하나로 움직일 수 있다.
# 코니와 브라운의 위치 p는 조건 0 <= x <= 200,000을 만족한다.
# 브라운은 범위를 벗어나는 위치로는 이동할 수 없고, 코니가 범위를 벗어나면 게임이 끝난다

# 11 (1) 12 (2) 14 (3) 17 (4) 21 (5) 26 (6) 32
# 즉, 코니의 n초후 위치는 c + sum(1:n)


c = 11
b = 2
 
def catch_me(cony_loc, brown_loc):
    time = 0
    queue = deque()
    queue.append((brown_loc, 0))
    visited = [{} for _ in range(200001)]

    while cony_loc < 200000:
        cony_loc += time

        if time in visited[cony_loc]:
            return time

        for i in range(0, len(queue)):
            curpos, curtime = queue.popleft()
            # b-1
            newtime = curtime + 1
            newposition = curpos - 1
            if newposition >= 0 and newtime not in visited[newposition]:
                visited[newposition][newtime] = True
                queue.append((newposition, newtime))

            newposition = curpos + 1
            if newposition < 200001 and newtime not in visited[newposition]:
                visited[newposition][newtime] = True
                queue.append((newposition, newtime))
            
            newposition = curpos * 2
            if newposition < 200001 and newtime not in visited[newposition]:
                visited[newposition][newtime] = True
                queue.append((newposition, newtime))

        time += 1

    return -1




print(catch_me(c, b))  # 5가 나와야 합니다!

print("정답 = 3 / 현재 풀이 값 = ", catch_me(10,3))
print("정답 = 8 / 현재 풀이 값 = ", catch_me(51,50))
print("정답 = 28 / 현재 풀이 값 = ", catch_me(550,500))