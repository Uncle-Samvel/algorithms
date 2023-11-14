'''
https://contest.yandex.ru/contest/45468/problems/27/
'''

n, m = map(int, input().split())
result = []
data = [[-1] * (m + 1)]

for i in range(n):
    data.append([-1] + list(map(int, input().split())))

data[1][0] = 0
data[0][1] = 0

for i in range(1, len(data)):
    for j in range(1, len(data[i])):
        data[i][j] = max(data[i - 1][j], data[i][j - 1]) + data[i][j]

i = len(data) - 1
j = len(data[i]) - 1

while (i == 1 and j == 1) == False:
    if data[i - 1][j] > data[i][j - 1]:
        result.append('D')
        i -= 1
    else:
        result.append('R')
        j -= 1

print(data[-1][-1])
print(*result[::-1])

