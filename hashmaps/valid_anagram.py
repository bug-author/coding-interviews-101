# https://leetcode.com/problems/valid-anagram/description/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = {}

        for char in s:
            if char in count_s:
                count_s[char] += 1
            else:
                count_s[char] = 1

        for char in t:
            if char in count_s:
                count_s[char] -= 1

            # boundary case: when a char is present in t but not in s
            # well, not a boundary case - I was just dumb to overlook this
            else:
                return False

        for i in count_s.values():
            if i != 0:
                return False

        return True
