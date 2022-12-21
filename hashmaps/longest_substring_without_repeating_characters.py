# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # sliding window
        # left and right pointer
        # right will go through each character

        charMap = {}
        maxL = 0
        start = 0
        for end in range(len(s)):
            while s[end] in charMap:
                charMap.pop(s[start])
                start += 1

            charMap[s[end]] = True

            maxL = max(maxL, end-start+1)

        return maxL
