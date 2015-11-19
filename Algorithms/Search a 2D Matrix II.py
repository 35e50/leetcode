class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for array in matrix:
            m = len(array)
            l, r = 0, m-1
            while l <= r:
                center = (l+r)/2
                if array[center] == target:
                    return True
                elif array[center] < target:
                    l = center+1
                else:
                    r = center-1
        return False