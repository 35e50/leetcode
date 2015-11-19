class Solution(object):
    def partition(self, nums, l, r):
        if l < r:
            pivot = nums[r]
            j = l-1
            for i in range(l, r):
                if nums[i] > pivot:
                    j = j + 1
                    nums[j], nums[i] = nums[i], nums[j]
            nums[j+1], nums[r] = nums[r], nums[j+1]
            return j+1
        
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        p = self.partition(nums, 0, len(nums)-1)
        if k == p+1:
            return nums[p]
        elif k < p+1:
            return self.findKthLargest(nums[:p], k)
        else:
            return self.findKthLargest(nums[p+1:], k-p-1)