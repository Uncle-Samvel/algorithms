'''
https://contest.yandex.ru/contest/29188/problems/E/
'''
n , k = map(int,input().split())
dots = sorted(list(map(int, input().split())))
l = 0
r = dots[-1] - dots[0]
while l < r:
    m = (l + r) // 2
    value = dots[0] + m
    num = 1
    for i in dots:
        if value < i:
            num += 1
            value = i + m
    if num > k:
        l = m + 1
    else:
        r = m
print(l)