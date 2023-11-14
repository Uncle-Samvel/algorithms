'''
https://contest.yandex.ru/contest/29403/problems/A/
'''

def add(tree: list[list[int]], value: int):
    if len(tree) == 1:
        tree[0] = [0, value, 0, 0]
        writer.write('DONE\n')

    else:
        index = 0
        head = tree[0]
        while 1:

            if value > head[1]:
                if head[3] != 0:
                    head = tree[head[3]]
                    index = head[3]
                else:
                    head[3] = len(tree) - 1
                    tree[-1] = [index,value,0,0]
                    writer.write('DONE\n')
                    break

            elif value < head[1]:
                if head[2] != 0:
                    head = tree[head[2]]
                    index = head[2]
                else:
                    head[2] = len(tree) - 1
                    tree[-1] = [index,value,0,0]
                    writer.write('DONE\n')
                    break

            else:
                writer.write('ALREADY\n')
                break



def search(tree: list[list[int]], value: int):
    if len(tree) == 0:
        writer.write('NO\n')
        return 0
    head = tree[0]
    while 1:

        if value > head[1]:
            if head[3] != 0:
                head = tree[head[3]]
            else:
                writer.write('NO\n')
                break

        elif value < head[1]:
            if head[2] != 0:
                head = tree[head[2]]
            else:
                writer.write('NO\n')
                break

        else:
            writer.write('YES\n')
            break

def printTree(tree: list[list[int]], depth,head):
    if head[2] != 0:
        printTree(tree,depth + 1,tree[head[2]])
    writer.write(depth * '.' + str(head[1]) + '\n')
    if head[3] != 0:
        printTree(tree,depth + 1,tree[head[3]])

tree = []
command = 1

reader = open('input.txt', 'r')
data = reader.readlines()
writer = open('output.txt', 'w')


for command in data:
    if command[-1] == '\n':
        command = command[:-1]
    command = list(command.split(' '))


    if len(command) == 1:
        printTree(tree,0,tree[0])
    elif len(command) == 2:
        command = [command[0], int(command[1])]
        if command[0] == 'ADD':
            tree.append([0, 0, 0, 0])
            add(tree,command[1])
        else:
            search(tree,command[1])

reader.close()
writer.close()

