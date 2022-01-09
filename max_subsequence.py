# https://leetcode.com/problems/maximum-subarray/
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_max = max_sum = current_sum = nums[0]

        for i in range(1, len(nums)):
            current_sum += nums[i]
            if current_sum < nums[i]:
                current_sum = nums[i]

            if current_max < current_sum:
                current_max = current_sum

            if current_sum <= 0:
                max_sum = max_sum if max_sum > current_max else current_max
                current_sum = max(0, nums[i])

        return max(max_sum, current_max)
