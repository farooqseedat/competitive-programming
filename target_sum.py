# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        elems = {}
        arr_size = len(nums)
        difference = 0
        for i in range(0, arr_size):
            elems[nums[i]] = i
        for i in range(0, arr_size):
            difference = target - nums[i]
            if elems.get(difference) and elems[difference] != i:
                return [i, elems[difference]]
