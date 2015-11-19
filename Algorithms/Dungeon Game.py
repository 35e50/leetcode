class Solution:
    # @param dungeon, a list of lists of integers
    # @return a integer
    def calculateMinimumHP(self, dungeon):
        m = len(dungeon); n = len(dungeon[0])
        d = [[0 for i in range(n)] for j in range(m)]
        d[m-1][n-1] = max(1-dungeon[m-1][n-1],1)
        for i in range(m-2,-1,-1):
            d[i][n-1] = max(d[i+1][n-1] - dungeon[i][n-1],1)
        for i in range(n-2,-1,-1):
            d[m-1][i] = max(d[m-1][i+1] - dungeon[m-1][i],1)
        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                a = max(d[i+1][j] - dungeon[i][j],1)
                b = max(d[i][j+1] - dungeon[i][j],1)
                d[i][j] = min(a,b)
        return d[0][0]