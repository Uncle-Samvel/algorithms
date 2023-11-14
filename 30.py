'''
https://contest.yandex.ru/contest/29188/problems/C/
'''

index = list(map(int, input().split()))
if index[0] < 0:
    for i in range(len(index)):
        index[i] = -index[i]

l = - 1000000
r = 1000000
eps = 0.00000000001

while l + eps < r:
    m = (l + r) / 2
    if m ** 3 * index[0] + m ** 2 * index[1] + m * index[2] + index[3] <= 0:
        l = m
    else:
        r = m
print(l)
