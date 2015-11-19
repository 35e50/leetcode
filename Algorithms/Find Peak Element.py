class Solution:
    # @param num, a list of integer
    # @return an integer
    def findPeakElement(self, num):
        if len(num) == 1: return 0
        for i in range(1, len(num)-1):
            if num[i] > num[i-1] and num[i] > num[i+1]:
                return i
        if num[0] > num[1]:
            return 0
        if num[len(num)-1] > num[len(num)-2]:
            return len(num)-1