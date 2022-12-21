# https://leetcode.com/problems/contains-duplicate/description/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        _map = {}

        for num in nums:
            if num in _map:
                return True
            else:
                _map[num] = 1

        return False
