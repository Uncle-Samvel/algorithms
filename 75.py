'''
https://contest.yandex.ru/contest/45468/problems/33/
'''


def dfs(graph, visited, now, color, lastcolor, flag):
    if visited[now] == False:
        visited[now] = True
        color[now] = 3 - lastcolor
        for neig in graph[now]:
            if color[neig] == color[now]:
                flag.append(0)
        for neig in graph[now]:
            if visited[neig] == False:
                dfs(graph, visited, neig, color, 3 - lastcolor, flag)


size = list(map(int, input().split()))

graph = [[]]
for i in range(size[0]):
    graph.append([])
visited = (size[0] + 1) * [False]
color = (size[0] + 1) * [0]
flag = []

for i in range(size[1]):
    start, stop = map(int, input().split())
    graph[start].append(stop)
    graph[stop].append(start)

for i in range(1,len(graph)):
    dfs(graph, visited, i, color, 1, flag)

if 0 in flag:
    print('NO')
else:
    print('YES')

