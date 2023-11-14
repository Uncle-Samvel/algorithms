'''
https://contest.yandex.ru/contest/29188/problems/B/
'''

x = input()
data = list(map(int, input().split()))
x = input()
search = list(map(int, input().split()))

for i in search:
    result = [0, 0]
    if data[0] <= i <= data[-1]:
        l = 1
        r = len(data)
        while l < r:
            m = (l + r) // 2
            if data[m - 1] >= i:
                r = m
            else:
                l = m + 1
        result[0] = l

        l = 1
        r = len(data)
        while l < r:
            m = (l + r + 1) // 2
            if data[m - 1] <= i:
                l = m
            else:
                r = m - 1
        result[1] = r
    if result[0] > result[1]:
        result = [0,0]
    print(*result)
