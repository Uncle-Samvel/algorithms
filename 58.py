'''
https://contest.yandex.ru/contest/45468/problems/11/
'''

command = list(input().split())
stack = []

while command[0] != 'exit':
    if len(command) == 1:
        if command[0] == 'size':
            print(len(stack))
        elif command[0] == 'back':
            if len(stack) != 0:
                print(stack[-1])
            else:
                print('error')
        elif command[0] == 'pop':
            if len(stack) != 0:
                print(stack[-1])
                stack.pop()
            else:
                print('error')
        elif command[0] == 'clear':
            stack = []
            print('ok')

    else:
         stack.append(command[1])
         print('ok')
    command = list(input().split())
print('bye')
