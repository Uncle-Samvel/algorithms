'''
https://contest.yandex.ru/contest/29075/problems/A
'''



param = [int(x) for x in input().split()]
start_stop = []

arr = [int(x) for x in input().split()]
sum = 0
arr_sum = [0]

for i in arr:
    sum += i
    arr_sum.append(sum)

for i in range(param[1]):
    start_stop += [[int(x) for x in input().split()]]

for i in start_stop:
    print(arr_sum[i[1]] - arr_sum[i[0] - 1])

