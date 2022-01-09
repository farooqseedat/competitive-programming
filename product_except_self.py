# https://leetcode.com/problems/product-of-array-except-self/
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = nums.copy()
        product = 1
        arr_size = len(nums)
        for i in range(0, arr_size):
            product = product * nums[i]
            answer[i] = product

        product = 1
        for i in range(arr_size-1, 0, -1):
            answer[i] = answer[i-1] * product
            product = product * nums[i]

        answer[0] = product
        return answer
