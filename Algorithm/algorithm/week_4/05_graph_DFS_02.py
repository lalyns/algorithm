# 위의 그래프를 예시로 삼아서 인접 리스트 방식으로 표현했습니다!
graph = {
    1: [2, 5, 9],
    2: [1, 3],
    3: [2, 4],
    4: [3],
    5: [1, 6, 8],
    6: [5, 7],
    7: [6],
    8: [5],
    9: [1, 10],
    10: [9]
}

def dfs_stack(adjacent_graph, start_node):
    
    visited = []
    stack = [start_node]


    # stack 내용물이 있으면 1 없으면 0 이라고 반환되는거잖아
    # syntax error

    while len(stack) > 0 :
    # while stack :
        cur_node = stack.pop()
        visited.append(cur_node)

        for adj_node in adjacent_graph[cur_node] :
            if adj_node not in visited :
                stack.append(adj_node)
        
    return visited


print(dfs_stack(graph, 1))  # 1 이 시작노드입니다!
# [1, 9, 10, 5, 8, 6, 7, 2, 3, 4] 이 출력되어야 합니다!