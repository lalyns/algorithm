
def solution(id_list, report, k):
    
    answer = [0] * len(id_list)
    report = list(set(report))

    report_dict = {}
    report_count = {}
    who_report_me = {}
    send_mail = {}
    
    for key in id_list:
        report_dict[key] = []
        who_report_me[key] = []
        report_count[key] = 0
        send_mail[key] = 0

    for index in range(len(report)) :
        temp = report[index].split(' ')
        key = temp[0]
        value = temp[1]
        report_dict[key].append(value)
        who_report_me[value].append(key)
        report_count[value] += 1

    suspended_id = [key for key, value in report_count.items() if value >= k]

    for i in suspended_id :
        aa = [value for key, value in who_report_me.items() if key == i]
        for a in aa :
            for i in a:
                send_mail[i] += 1
    
    for i in range(len(id_list)) :
        answer[i] = send_mail[id_list[i]]
    
    return answer
