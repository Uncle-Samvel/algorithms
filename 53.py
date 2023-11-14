'''
https://leetcode.com/problems/two-sum/
'''


def search(nums : list[int],target : int) -> list[int]:
    dict = {}
    for i in range(len(nums)):
        if nums[i] not in dict:
            dict[nums[i]] = [i]
        else:
            dict[nums[i]].append(i)

    for i in range(len(nums)):
        if target - nums[i] in dict:
            if target != 2 * nums[i]:
                return [i, nums.index(target - nums[i])]
            elif len(dict[nums[i]]) > 1:
                return [dict[nums[i]][0],dict[nums[i]][1]]
