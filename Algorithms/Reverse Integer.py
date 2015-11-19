class Solution:
    # @return an integer
    def reverse(self, x):
        answer = 0
        sign = 1
        if x < 0:
            x = -x
            sign = -1
        while x > 0:
            answer = answer * 10 + x % 10
            x /= 10
        return sign*answer