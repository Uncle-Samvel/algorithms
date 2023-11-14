'''
https://contest.yandex.ru/contest/45468/problems/14/
'''

amount = int(input())
stack = []
train = list(map(int, input().split()))
pred = 0
flag_2 = True

for i in train:
    if len(stack) != 0:
        flag = False
        while flag == False:
            if len(stack) != 0 and i > stack[-1]:
                if pred > stack[-1] and flag_2 != False:
                    flag_2 = False
                    print('NO')
                    break
                pred = stack[-1]
                stack.pop()
            else:
                flag = True
                stack.append(i)
    else:
        stack.append(i)

if flag_2 == True:

    value = stack[-1] - 1

    while len(stack) != 0:
        if stack[-1] - 1 != value:
            print('NO')
            break

        else:
            value = stack[-1]
            stack.pop()

    if value == amount:
        print('YES')
