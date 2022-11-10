shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]

# 내림차순 정렬 후 각각 요소를 곱해준다

def get_max_discounted_price(prices, coupons):
    prices.sort(reverse=True)
    coupons.sort(reverse=True)

    cost = 0
    
    p_index = 0
    c_index = 0

    while p_index < len(prices) and c_index < len(coupons) :
        discount = 1 - coupons[c_index] / 100  # *0.01 일시, 3번 TC에서 484999 찍힘
        cost += prices[p_index] * discount
        p_index += 1
        c_index += 1
    
    while p_index < len(prices) :
        cost += prices[p_index]
        p_index += 1

    cost = int(cost)

    return cost


print("정답 = 926000 / 현재 풀이 값 = ", get_max_discounted_price([30000, 2000, 1500000], [20, 40]))
print("정답 = 485000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], [10, 70, 30, 20]))
print("정답 = 1550000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], []))
print("정답 = 1458000 / 현재 풀이 값 = ", get_max_discounted_price([20000, 100000, 1500000], [10, 10, 10]))