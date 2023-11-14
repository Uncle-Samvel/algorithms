'''
https://contest.yandex.ru/contest/45468/problems/18/
'''

command = list(input().split())
dec = []

while command[0] != 'exit':
    if len(command) == 1:

        if command[0] == 'size':
            print(len(dec))


        elif command[0] == 'front':
            if len(dec) != 0:
                print(dec[0])
            else:
                print('error')

        elif command[0] == 'back':
            if len(dec) != 0:
                print(dec[-1])
            else:
                print('error')


        elif command[0] == 'pop_front':
            if len(dec) != 0:
                print(dec[0])
                dec.pop(0)
            else:
                print('error')

        elif command[0] == 'pop_back':
            if len(dec) != 0:
                print(dec[-1])
                dec.pop()
            else:
                print('error')


        elif command[0] == 'clear':
            dec = []
            print('ok')

    else:

        if command[0] == 'push_front':
            dec = [command[1]] + dec
            print('ok')

        elif command[0] == 'push_back':
            dec.append(command[1])
            print('ok')

    command = list(input().split())
print('bye')
