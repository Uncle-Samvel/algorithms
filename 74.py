'''
https://contest.yandex.ru/contest/45468/problems/31/
'''

from sys import setrecursionlimit
setrecursionlimit(200000)

def dfs(graph, now, visited, linked, linkedValue,counter,visitedIndex):
    visited[now] = True
    linked[now] = linkedValue
    visitedIndex.append(now)
    counter += 1
    for neig in graph[now]:
        if visited[neig] == False:
            counter = (dfs(graph, neig, visited, linked, linkedValue,counter,visitedIndex))[0]
    return [counter, visitedIndex]


size = list(map(int, input().split()))

graph = [[]]
for i in range(size[0]):
    graph.append([])
visited = (size[0] + 1) * [False]
linked = (size[0] + 1) * [0]

for i in range(size[1]):
    start, stop = map(int, input().split())
    graph[start].append(stop)
    graph[stop].append(start)

linkedValue = 1
index = 1
result = []

while 1:
    visitedIndex = []
    result.append(dfs(graph, index, visited, linked, linkedValue,0,visitedIndex))

    while index < len(linked):
        if linked[index] == 0:
            break
        else:
            index += 1

    linkedValue += 1

    if index == len(linked):
        break

print(len(result))
for i in result:
    print(i[0])
    print(*i[1])
