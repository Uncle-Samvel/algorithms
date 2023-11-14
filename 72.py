'''
https://contest.yandex.ru/contest/28738/problems/D/
'''

tables = list(map(int, input().split()))
blocks = list(map(int, input().split()))

center = tables[0] / 2

if blocks[-1] + 0.5 == (tables[0] / 2):
    print(blocks[-1])
elif len(blocks) == 1:
    print(blocks[0])
else:
    i = 0
    while i < len(blocks):
        if blocks[i] > center:
            if blocks[i - 1] + 0.5 == tables[0] / 2:
                print(blocks[i - 1])
                break
            else:
                print(blocks[i - 1], blocks[i])
                break
        if blocks[i] == center:
            print(blocks[i - 1], blocks[i])
            break
        i += 1