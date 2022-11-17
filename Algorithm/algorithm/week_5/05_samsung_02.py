from collections import deque

game_map = [
    ["#", "#", "#", "#", "#"],
    ["#", ".", ".", "B", "#"],
    ["#", ".", "#", ".", "#"],
    ["#", "R", "O", ".", "#"],
    ["#", "#", "#", "#", "#"],
]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def move_until_wall_or_hole(r, c, diff_r, diff_c, game_map):
    move_count = 0
    while game_map[r + diff_r][c + diff_c] != '#' and game_map[r][c] != 'O':
        r += diff_r
        c += diff_c
        move_count += 1
    return r, c, move_count

def is_available_to_take_out_only_red_marble(game_map):
    # 구현해보세요!
    n, m = len(game_map), len(game_map[0])

    visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
    red_r, red_c, blue_r, blue_c = -1, -1, -1, -1
    for i in range(n):
        for j in range(m):
            if game_map[i][j] == 'R' :
                red_r, red_c = i, j
            elif game_map[i][j] == 'B' :
                blue_r, blue_c = i, j

    queue = deque()
    queue.append((red_r, red_c, blue_r, blue_c, 1))
    visited[red_r][red_c][blue_r][blue_c] = True
    while queue :
        red_r, red_c, blue_r, blue_c, try_count = queue.popleft()
        if try_count > 10:
            break

        for i in range(4):
            next_red_r, next_red_c, red_move_count = move_until_wall_or_hole(red_r, red_c, dr[i], dc[i], game_map)
            next_blue_r, next_blue_c, blue_move_count = move_until_wall_or_hole(blue_r, blue_c, dr[i], dc[i], game_map)

            if game_map[next_blue_r][next_blue_c] == 'O' :
                continue
            if game_map[next_red_r][next_red_c] == 'O' :
                return True
            if next_red_r == next_blue_r and next_red_c == next_blue_c :
                if red_move_count > blue_move_count:
                    next_red_r -= dr[i]
                    next_red_c -= dc[i]
                else :
                    next_blue_r -= dr[i]
                    next_blue_c -= dc[i]

            if not visited[next_red_r][next_red_c][next_blue_r][next_blue_c] :
                visited[next_red_r][next_red_c][next_blue_r][next_blue_c] = True
                queue.append((next_red_r, next_red_c, next_blue_r, next_blue_c, try_count+1))

    return False


print(is_available_to_take_out_only_red_marble(game_map))  # True 를 반환해야 합니다



game_map = [
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", ".", "O", ".", ".", ".", ".", "R", "B", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]
]
print("정답 = False / 현재 풀이 값 = ", is_available_to_take_out_only_red_marble(game_map))


game_map = [
["#", "#", "#", "#", "#", "#", "#"],
["#", ".", ".", "R", "#", "B", "#"],
["#", ".", "#", "#", "#", "#", "#"],
["#", ".", ".", ".", ".", ".", "#"],
["#", "#", "#", "#", "#", ".", "#"],
["#", "O", ".", ".", ".", ".", "#"],
["#", "#", "#", "#", "#", "#", "#"]
]
print("정답 = True / 현재 풀이 값 = ", is_available_to_take_out_only_red_marble(game_map))