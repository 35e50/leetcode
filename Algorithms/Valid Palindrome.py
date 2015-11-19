class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        if s == '':
            return True
        else:
            sTmp = ''
            for i in range(0, len(s)):
                if s[i] >= 'a' and s[i] <= 'z' or s[i] >= '0' and s[i] <= '9' or s[i] >= 'A' and s[i] <= 'Z':
                    sTmp += s[i]
            sTmp = sTmp.lower()
            for i in range(0, len(sTmp)/2):
                if sTmp[i] != sTmp[len(sTmp)-1-i]:
                    return False
            return True