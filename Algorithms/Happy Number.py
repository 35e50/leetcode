class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s = set()
        while n != 1:
            n = self.Sum(n)
            if n in s:
                return False
            else:
                s.add(n)
        return True
            
    def Sum(self, n):
        Sum = 0
        while n != 0:
            Sum = Sum + (n-(n/10)*10) ** 2
            n = n/10
        return Sum