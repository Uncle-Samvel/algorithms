'''
https://contest.yandex.ru/contest/45468/problems/24/
'''

amount = int(input())
A = []
B = []
C = []

for i in range(amount):
    time = list(map(int, input().split()))
    A.append(time[0])
    B.append(time[1])
    C.append(time[2])

if len(A) == 1:
    print(A[0])
elif len(A) == 2:
    print(min(A[0] + A[1], B[0]))
elif len(A) == 3:
    print(min(A[0] + A[1] + A[2], B[0] + A[2], A[0] + B[1], C[0]))
else:
    dp = amount * [0]

    dp[0] = A[0]
    dp[1] = min(A[0] + A[1], B[0])
    dp[2] = min(A[0] + A[1] + A[2], B[0] + A[2], A[0] + B[1], C[0])

    for i in range(3, amount):
        dp[i] = min(dp[i - 1] + A[i], dp[i - 2] + B[i - 1], dp[i - 3] + C[i - 2])
    print(dp[-1])
