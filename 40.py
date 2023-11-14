'''
https://leetcode.com/problems/subarray-sum-equals-k/description/
'''

nums = [1, 2, 3]


def search(nums: list[int], k: int) -> int:
    if len(nums) == 1 and nums[0] != k:
        return 0
    dict = {0: 1}
    prefix = 0
    counter = 0
    for item in nums:
        prefix += item

        if (prefix - k) in dict:
            counter += dict[prefix - k]

        if prefix not in dict:
            dict[prefix] = 1
        else:
            dict[prefix] += 1

    return counter

print(search(nums, 3))
