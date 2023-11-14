'''
https://contest.yandex.ru/contest/45468/problems/15/
'''


n = int(input())

data = list(map(int,input().split()))
stack = []
result = [-1] * n

for i in range(len(data)):
    if len(stack) != 0:
        while len(stack) != 0 and data[i] < stack[-1][0]:
            result[stack[-1][1]] = i
            stack.pop()
        stack.append([data[i],i])
    else:
        stack.append([data[i],i])

print(*result)