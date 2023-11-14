'''
https://contest.yandex.ru/contest/45468/problems/19/
'''

heap = []
amountCommand = int(input())

for i in range(amountCommand):
    command = list(map(int, input().split()))
    if len(command) == 1:
        print(heap[0])
        heap[0] = heap[-1]
        index = 0
        while index * 2 + 2 < len(heap):
            maxSon = index * 2 + 1
            if heap[maxSon] < heap[maxSon + 1]:
                maxSon += 1
            if heap[index] < heap[maxSon]:
                heap[index], heap[maxSon] = heap[maxSon], heap[index]
                index = maxSon
            else:
                break
        heap.pop()
    else:
        heap.append(command[1])
        index = len(heap) - 1

        while index > 0 and heap[index] > heap[(index - 1) // 2]:
            heap[index], heap[(index - 1) // 2] = heap[(index - 1) // 2], heap[index]
            index = (index - 1) // 2
