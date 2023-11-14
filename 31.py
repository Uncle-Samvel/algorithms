'''
https://contest.yandex.ru/contest/29188/problems/D/
'''

k = list(map(int,input().split()))

l = 0
r = k[4] * 2 // k[0] + 1

while l < r:
    m = (l + r)//2
    if m*(k[0] + k[2]) - (m//k[1])*k[0] - (m//k[3])*k[2] < k[4]:
        l = m + 1
    else:
        r = m

print(l)