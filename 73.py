'''
https://contest.yandex.ru/contest/45468/problems/31/
'''


def dfs(graph, visited, now, linked):
    visited[now] = True
    linked[now] = 1
    for neig in graph[now]:
        if not visited[neig]:
            dfs(graph, visited, neig, linked)


x = list(map(int, input().split()))

graph = [[]]
for i in range(x[0]):
    graph.append([])
visited = [0] + x[0] * [False]
linked = [0] + x[0] * [0]


for i in range(x[1]):
    data = list(map(int, input().split()))
    if data[0] != data[1]:
        graph[data[0]] += [data[1]]
        graph[data[1]] += [data[0]]
    data.clear()

dfs(graph, visited, 1, linked)

print(sum(linked))

for i in range(1, len(linked)):
    if linked[i] == 1:
        print(i, end=' ')
