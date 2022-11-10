shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두", "치즈스틱"]


def is_available_to_order(menus, orders):
    # menu = menus
    # menu.sort()
    # for aaa in orders:
    #     low = 0;
    #     high = len(menu) - 1
    #     order = False;

    #     while low <= high :
    #         mid = (low+high) // 2
    #         if menu[mid] == aaa :
    #             order = True
    #             low = high + 1; # while문을 탈출하기 위한 조건 변경
    #         elif menu[mid] > aaa :
    #             high = mid - 1
    #         else :
    #             low = mid + 1

    #     if not order :
    #         return False
    # 이 부분을 채워보세요!

    orderSet = set(orders)
    menuSet = set(menus)

    if len(orderSet.difference(menuSet)) == 0 :
        return True
    else :
        return False

result = is_available_to_order(shop_menus, shop_orders)
print(result)