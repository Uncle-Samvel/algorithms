'''
https://contest.yandex.ru/contest/28964/problems/E/
'''


max = 0
result = []
amount_1 = int(input())
arr_1 = []

for i in range(amount_1):
    arr_1.append(input())

amount_2 = int(input())

for i in range(amount_2):
    example = input()
    num = 0
    for j in arr_1:
        if set(example) >= set(j):
            num += 1

    if num > max:
        result = []
        result.append(example)
        max = num
    elif num == max:
        result.append(example)

print('\n'.join(result))





