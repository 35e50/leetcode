class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        list = str.split(" ")
        if len(pattern) != len(list):
            return False
        dict = {}
        unique = set()
        for i in range(len(pattern)):
            if pattern[i] not in dict.keys() and list[i] not in unique:
                dict[pattern[i]] = list[i]
                unique.add(list[i])
            elif pattern[i] not in dict.keys() and list[i] in unique:
                return False
            elif pattern[i] in dict.keys() and list[i] != dict[pattern[i]]:
                return False
        return True