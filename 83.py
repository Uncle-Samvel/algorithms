'''
https://contest.yandex.ru/contest/45468/problems/37/
'''

amount_peaks = int(input())

graph = [[0]]
for i in range(amount_peaks):
    graph.append([])

for i in range(amount_peaks):
    line = list(map(int, input().split()))
    for value in range(len(line)):
        if line[value] == 1:
            graph[i + 1].append(value + 1)

start, stop = map(int, input().split())
path = [-1] * (amount_peaks + 1)
pred = [-1] * (amount_peaks + 1)
pred[start] = 0
stack_start = [start]
stack_stop = []

lenght = 0
while len(stack_start) != 0:
    for item in stack_start:
        path[item] = lenght
        for i in graph[item]:
            if path[i] == -1:
                stack_stop.append(i)
                if pred[i] == -1:
                    pred[i] = item
    stack_start = stack_stop
    stack_stop = []
    if path[stop] != -1:
        break
    lenght += 1

print(path[stop])
if path[stop] != -1 and path[stop] != 0:
    item = stop
    result = []
    while item != 0:
        result.append(item)
        item = pred[item]
    print(*result[::-1])
