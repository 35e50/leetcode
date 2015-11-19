class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 0:
            return 0
        if length == 1:
            return nums[0]
        list = [0 for i in range(length+1)]
        list[0] = 0
        list[1] = nums[0]
        for i in range(2,length+1):
            list[i] = max(list[i-2]+nums[i-1], list[i-1])
        return list[-1]