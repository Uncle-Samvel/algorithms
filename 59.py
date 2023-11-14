'''
https://contest.yandex.ru/contest/45468/problems/13/
'''

str = input().split()
stack = []
for i in str:
    if i == '+':
        a = stack[-1]
        b = stack[-2]
        stack.pop()
        stack.pop()
        stack.append(a + b)
    elif i == '-':
        a = stack[-1]
        b = stack[-2]
        stack.pop()
        stack.pop()
        stack.append(b - a)
    elif i == '*':
        a = stack[-1]
        b = stack[-2]
        stack.pop()
        stack.pop()
        stack.append(a * b)
    else:
        stack.append(int(i))
print(stack[0])
