'''
https://contest.yandex.ru/contest/45468/problems/34/
'''
from sys import setrecursionlimit
setrecursionlimit(200000)

def dfs(graph,visited,now,result,flag):
    visited[now] = 0
    for neig in graph[now]:
        if visited[neig] == -1:
            dfs(graph,visited,neig,result,flag)
        elif visited[neig] == 0:
            flag.append(0)
    visited[now] = 1
    result.append(now)

size = list(map(int, input().split()))

graph = [[]]
for i in range(size[0]):
    graph.append([])
visited = (size[0] + 1) * [-1]
flag = []

for i in range(size[1]):
    start, stop = map(int, input().split())
    graph[start].append(stop)

result = []

for i in range(1,len(visited)):
    if visited[i] == -1:
        dfs(graph,visited,i,result,flag)

if 0 not in flag:
    print(*result[::-1])
else:
    print(-1)