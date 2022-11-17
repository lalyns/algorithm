id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
k = 2

from collections import deque

def solution(id_list, report, k):
    answer = [0] * len(id_list)
    report_count = [0] * len(id_list)
    id_index = {}
    i = 0
    for key in id_list:
        id_index[key] = i
        i += 1
    report = list(set(report))

    who_report_me = {}
    for key in id_list :
        who_report_me[key] = []
    
    for aaa in report :
        temp = aaa.split(' ')
        who_report_me[temp[1]].append(temp[0])
        report_count[id_index[temp[1]]] += 1

    queue = deque()

    for i in range(len(report_count)):
        if report_count[i] >= k :
            for v in who_report_me[id_list[i]]:
                queue.append(v)

    while queue :
        key = queue.popleft()
        answer[id_index[key]] += 1
    return answer

print(solution(id_list, report, k))