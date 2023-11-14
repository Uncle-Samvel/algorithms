'''
https://leetcode.com/problems/longest-substring-without-repeating-characters/
'''

s = "aabaab!bb"

def lengthOfLongestSubstring(s: str) -> int:
    maxSub = 0
    counter = 0
    string = ''
    dictStr = {}
    for i in range(len(s)):
        if s[i] not in dictStr:
            dictStr[s[i]] = i
            counter += 1
            maxSub = max(counter, maxSub)
            string += s[i]
        elif dictStr[s[i]] != -1:
            while string[0] != s[i]:
                dictStr[string[0]] = -1
                counter -= 1
                string = string[1:]
            dictStr[string[0]] = i
            string = string[1:]
            string += s[i]
        elif dictStr[s[i]] == -1:
            dictStr[s[i]] = i
            counter += 1
            string += s[i]
            maxSub = max(counter, maxSub)
    return maxSub

print(lengthOfLongestSubstring(s))