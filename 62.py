'''
https://contest.yandex.ru/contest/45468/problems/16/
'''

command = list(input().split())
queue = []

while command[0] != 'exit':
    if len(command) == 1:
        if command[0] == 'size':
            print(len(queue))
        elif command[0] == 'front':
            if len(queue) != 0:
                print(queue[0])
            else:
                print('error')
        elif command[0] == 'pop':
            if len(queue) != 0:
                print(queue[0])
                queue.pop(0)
            else:
                print('error')
        elif command[0] == 'clear':
            queue = []
            print('ok')

    else:
         queue.append(command[1])
         print('ok')
    command = list(input().split())
print('bye')