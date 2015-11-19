class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return 0
        stack = []
        for i in s:
            stack.append(i)
        while stack and stack[-1] == " ":
            stack.pop()
        count = 0
        while stack and stack.pop() != " ":
            count += 1
        return count

class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        return len(s.split()[len(s.split())-1]) if s.split() != [] else 0