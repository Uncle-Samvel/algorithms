'''
https://contest.yandex.ru/contest/45468/problems/22/
'''

n, k = map(int, input().split())

dp = n * [0]
dp[0] = 1

if k >= n:
    k = n - 1

for i in range(1, k + 1):
    dp[i] = 2 ** (i - 1)

for i in range(k + 1, n):
    dp[i] = sum(dp[i - k:i])

print(dp[-1])
