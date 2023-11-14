'''
https://contest.yandex.ru/contest/29075/problems/B/
'''

amount = int(input())

arr = list(map(int, input().split()))
sum = 0
arr_sum = []
new_arr = []
value = 0


for i in arr:
    sum += i
    if sum < 0:
        sum = 0
    arr_sum.append(sum)

if set(arr_sum) == {0}:
    print(max(arr))
else:
    print(max(arr_sum))
