class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = [1] * len(nums)
        tmp = 1
        for i in range(1, len(nums)):
            tmp = tmp * nums[i-1]
            output[i] = output[i] * tmp
        tmp = 1
        for i in range(len(nums)-2, -1, -1):
            tmp = tmp * nums[i+1]
            output[i] = output[i] * tmp
        return output