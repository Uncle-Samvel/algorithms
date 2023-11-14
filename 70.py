'''
https://contest.yandex.ru/contest/45468/problems/26/
'''

n, m = map(int, input().split())

data = [[1000] * (m + 1)]

for i in range(n):
    data.append([1000] + list(map(int, input().split())))

data[1][0] = 0
data[0][1] = 0

for i in range(1, len(data)):
    for j in range(1, len(data[i])):
        data[i][j] = min(data[i - 1][j], data[i][j - 1]) + data[i][j]

print(data[-1][-1])
