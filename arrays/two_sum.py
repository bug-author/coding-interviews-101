# https://leetcode.com/problems/two-sum/description/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = [-1, -1]
        visited = {}

        for i, num in enumerate(nums):
            if target - num in visited:
                ans[0] = i
                ans[1] = visited[target - num]
                break

            else:
                visited[num] = i

        return ans
