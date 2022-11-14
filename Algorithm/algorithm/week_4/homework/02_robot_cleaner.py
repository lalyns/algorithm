current_r, current_c, current_d = 7, 4, 0
current_room_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

#up = row -1
#down = row +1
#left = col -1
#right = col +1
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def rotate(n) :
    return (n + 3) % 4

def back(n) :
    return (n + 2) % 4

def get_count_of_departments_cleaned_by_robot_vacuum(r, c, d, room_map):

    n = len(room_map)
    m = len(room_map[0])
    count = 1
    room_map[r][c] = 2
    queue = list([[r,c,d]])

    while queue :
        r, c, d = queue.pop(0)
        temp_d = d

        for i in range(4) :
            temp_d = rotate(temp_d)
            new_r, new_c = r + dr[temp_d], c + dc[temp_d]

            if 0 <= new_r < n and 0 <= new_c < m and room_map[new_r][new_c] == 0 :
                count += 1
                room_map[new_r][new_c] = 2
                queue.append([new_r, new_c, temp_d])
                break
            
            elif i == 3:
                new_r, new_c = r + dr[back(d)], c + dc[back(d)]
                queue.append([new_r, new_c, d])

                if room_map[new_r][new_c] == 1:
                    return count

    return


# 57 가 출력되어야 합니다!
print(get_count_of_departments_cleaned_by_robot_vacuum(current_r, current_c, current_d, current_room_map))