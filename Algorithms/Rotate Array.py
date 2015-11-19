class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # if k == 0: return
        l = len(nums) - k % len(nums)
        self.reverse(nums, 0, l-1)
        self.reverse(nums, l, len(nums)-1)
        self.reverse(nums, 0, len(nums)-1)
        
    def reverse(self, nums, start, end):
        for i in range(start, (start+end)/2+1):
            nums[i], nums[end+start-i] = nums[end+start-i], nums[i]