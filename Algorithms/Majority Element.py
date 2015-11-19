class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        dict = {}
        for integer in num:
            dict[integer] = dict.get(integer, 0) + 1
            if dict[integer] > len(num)/2:
                return integer