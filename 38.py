'''
https://leetcode.com/problems/summary-ranges/description/
'''

nums = [0,1,2,4,5,7]


def search(nums):
    result = []
    start = -1

    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1] + 1:
            if start == -1:
                start = nums[i - 1]
        elif nums[i] != nums[i - 1] and start != -1:
            result.append([start, nums[i - 1]])
            start = -1
        else:
            result.append([nums[i - 1]])

    if start != -1:
        result.append([start, nums[-1]])
    elif nums[len(nums) - 1] != nums[len(nums) - 2] + 1:
        result.append([nums[len(nums) - 1]])

    for i in range(len(result)):
        if len(result[i]) == 2:
            result[i] = str(result[i][0]) + '->' + str(result[i][1])
        else:
            result[i] = str(result[i][0])


    return result


print(search(nums))
