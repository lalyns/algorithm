seat_count = 9
vip_seat_array = [4, 7]

memo = {
    1: 1,
    2: 1
}


def fibo_dynamic_programming(n, fibo_memo):
    if n in fibo_memo:
        return fibo_memo[n]

    nfibo = fibo_dynamic_programming(n-1, fibo_memo) + fibo_dynamic_programming(n-2, fibo_memo) 
    fibo_memo[n] = nfibo

    return nfibo

def get_all_ways_of_theater_seat(total_count, fixed_seat_array):

    remain_changeable_seats_array = []

    for index in range(len(fixed_seat_array) + 1) :
        if index == 0 :
            remain_changeable_seats_array.append(fixed_seat_array[index] - 1)
        elif index == len(fixed_seat_array) :
            remain_changeable_seats_array.append(total_count - fixed_seat_array[index - 1])
        else :
            remain_changeable_seats_array.append(fixed_seat_array[index] - fixed_seat_array[index - 1] - 1)

    answer = 1

    for index in range(len(remain_changeable_seats_array)) :
        answer *= fibo_dynamic_programming(remain_changeable_seats_array[index] + 1, memo)

    return answer


# 12가 출력되어야 합니다!
print(get_all_ways_of_theater_seat(seat_count, vip_seat_array))