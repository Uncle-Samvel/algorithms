'''
https://contest.yandex.ru/contest/45468/problems/23/
'''

n = int(input())
x = [-1] * (n + 1)
dp = [0] * (n + 1)

for i in range(2, n + 1):
    v = dp[i - 1]
    x[i] = i - 1
    if i % 2 == 0:
        if v > dp[i // 2]:
            v = dp[i // 2]
            x[i] = i // 2

    if i % 3 == 0:
        if v > dp[i // 3]:
            v = dp[i // 3]
            x[i] = i // 3

    dp[i] = v + 1

print(dp[-1])
result = []
index = n
while index != -1:
    result.append(index)
    index = x[index]

print(*result[::-1])

#  0  1 2 3 4 5 6
# -1 -1 1 1 2 4 2
