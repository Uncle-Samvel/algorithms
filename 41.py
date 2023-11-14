'''
https://leetcode.com/problems/move-zeroes/description/
'''


def zero(nums: list(int)) -> None:
    counter = 0
    i = 0
    while i < len(nums) - 1:
        if nums[i] == 0:
            counter += 1
            nums.pop(i)
    for i in range(counter):
        nums.append(0)


nums = [0, 1, 2, 3, 4, 5, 0, 0, 1]
zero(nums)
print(nums)
