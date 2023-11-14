'''
https://contest.yandex.ru/contest/28736/problems/E/
'''


def intersection(rect1, rect2):
    x_left = max(rect1[0], rect2[0])
    y_top = max(rect1[1], rect2[1])
    x_right = min(rect1[2], rect2[2])
    y_bottom = min(rect1[3], rect2[3])
    if x_left < x_right and y_top < y_bottom:
        return (x_left, y_top, x_right, y_bottom)
    else:
        return 0


def check_circle(x, y, X, Y, r):
    if (x - X) ** 2 + (y - Y) ** 2 <= r ** 2:
        return (1)
    return (0)


shorn = [int(x) for x in input().split()]
water = [int(x) for x in input().split()]
ans = 0
rect1 = [shorn[0], shorn[1], shorn[2], shorn[3]]
rect2 = [water[0] - water[2], water[1] + water[2], water[0] + water[2], water[1] - water[2]]
area = intersection(rect1,rect2)
if area == 0:
    pass
else:
    for Y in range(area[3], shorn[1] + 1):
        for X in range(area[0], area[2] + 1):
            if check_circle(water[0], water[1], X, Y, water[2]) == 1:
                ans += 1

print(ans)
