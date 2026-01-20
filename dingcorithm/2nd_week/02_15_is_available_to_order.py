shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"] 

def is_available_to_order(menus, orders):
    sorted_menus = sorted(menus)

    for order in orders:
        left = 0
        right = len(sorted_menus) - 1
        is_found = False
        while left <= right:
            mid = (left+right) // 2
            if sorted_menus[mid] == order:
                is_found = True
                break
            elif sorted_menus[mid] < order:
                left = mid + 1
            else:
                right = mid - 1
        if not is_found:
            return False
    else:
        return True


result = is_available_to_order(shop_menus, shop_orders)
print(result)