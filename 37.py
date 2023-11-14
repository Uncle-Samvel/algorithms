'''
https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/description/
'''

nums = [1,0,0,1,1,1,1,1,0,0,0,0,0,0,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,0,0,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,1,1,1,1,0,1,1]


def search(nums):
    if nums == len(nums) * [1]:
        return (len(nums) - 1)

    data = []
    counter = 0
    maxValue = 0

    for i in range(len(nums)):
        if i == len(nums) - 1:
            if nums[i - 1] == nums[i]:
                if nums[i] == 0:
                    counter += 1
                    data.append(-counter)
                else:
                    counter += 1
                    data.append(counter)
            else:

                data.append(nums[i])


        else:
            if nums[i] == nums[i + 1]:
                counter += 1
            else:
                if nums[i] == 1:
                    data.append(counter + 1)
                elif nums[i] == 0 and counter != 0:
                    data.append(-(counter + 1))
                else:
                    data.append(0)
                counter = 0

    for i in range(len(data)):
        if data[i] == 0 and i != (len(data) - 1) and i != 0:
            value = data[i - 1] + data[i + 1]
            maxValue = max(value, maxValue)

    if maxValue < max(data):
        maxValue = max(data)

    if maxValue < 0:
        return 0
    print(data)
    return maxValue


print(search(nums))
