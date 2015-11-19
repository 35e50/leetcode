class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if len( strs ) == 0:
            return ''
        if len( strs ) == 1:
            return strs[0]
        minstrslen = 9999
        index = 0
        for i in range( 0, len( strs ) ):
            if len( strs[i] ) < minstrslen:
                minstrslen = len( strs[i] )
                index = i
        ShortestString = strs[index]
        list = [0 for i in range( len( ShortestString ) )]
        for i in range(0, len( ShortestString )):
            for j in range(0, len( strs )):
                if strs[j][i] == ShortestString[i]:
                    list[i] += 1
        Prefix = ''
        for i in range(0, len( ShortestString )):
            if list[i] == len( strs ):
                Prefix += ShortestString[i]
            else:
                break
        return Prefix