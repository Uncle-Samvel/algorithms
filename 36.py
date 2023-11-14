'''
https://contest.yandex.ru/contest/29396/problems/D/
'''

n, m = map(int, input().split())
cats = list(map(int, input().split()))
counter = 0
line = []
result = m * [0]

for i in range(m):
    start, stop = map(int, input().split())
    line.append([start, -1, i])
    line.append([stop, 1, i])

for i in cats:
    line.append([i, 0])

line.sort()

for event in line:
    if event[1] == -1:
        result[event[2]] -= counter
    elif event[1] == 1:
        result[event[2]] += counter
    else:
        counter += 1

print(*result)
