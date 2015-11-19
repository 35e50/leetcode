class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num/10 == 0:
            return num
        sum = 0
        while num/10 != 0:
            sum = sum + num - (num/10) * 10
            num = num/10
        sum = sum + num
        return self.addDigits(sum)