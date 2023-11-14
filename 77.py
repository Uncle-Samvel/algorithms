'''
https://contest.yandex.ru/contest/45468/problems/35/
'''

from sys import setrecursionlimit
setrecursionlimit(200000)


def dfs(graph, visited, now, result, stack, pred):
    visited[now] = 0
    stack.append(now)
    for neig in graph[now]:
        if visited[neig] == -1:
            dfs(graph, visited, neig, result, stack, now)
        elif visited[neig] == 0 and neig != pred:
            result.append(stack[stack.index(neig):])
    visited[now] = 1
    stack.pop()


size = list(map(int, input().split()))

graph = [[]]
for i in range(size[0]):
    graph.append([])
visited = (size[0] + 1) * [-1]
flag = []

for i in range(size[0]):
    line = list(map(int, input().split()))
    for j in range(len(line)):
        if line[j] == 1:
            graph[i + 1].append(j + 1)

result = []
stack = []

for i in range(1, len(visited)):
    if visited[i] == -1:
        dfs(graph, visited, i, result, stack, 0)

if len(result) != 0:
    result = result[0]
    print('YES')
    print(len(result))
    print(*result)
else:
    print('NO')
