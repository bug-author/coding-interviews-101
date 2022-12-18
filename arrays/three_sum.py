# https://leetcode.com/problems/3sum/description/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # neccesary to prevent duplicates
        output = []

        for first_idx in range(0, len(nums) - 2):
            if first_idx > 0 and nums[first_idx - 1] == nums[first_idx]:
                continue

            second_idx, third_idx = first_idx + 1, len(nums) - 1
            while second_idx < third_idx:
                if nums[first_idx] + nums[second_idx] + nums[third_idx] == 0:
                    output.append(
                        [nums[first_idx], nums[second_idx], nums[third_idx]])
                    second_idx += 1
                    while second_idx < third_idx and nums[second_idx-1] == nums[second_idx]:
                        second_idx += 1

                elif nums[first_idx] + nums[second_idx] + nums[third_idx] < 0:
                    second_idx += 1
                else:
                    third_idx -= 1
        return output
