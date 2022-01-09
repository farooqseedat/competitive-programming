# https://leetcode.com/problems/contains-duplicate/
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        elements = {}
        for num in nums:
            if elements.get(num, None) != None:
                return True
            elements[num] = num
        return False
