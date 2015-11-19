class Solution:
    # @return a string
    # def dfs(self, n, k, string, stringlist):
    #     if len(stringlist) == n: 
    #         Solution.count += 1
    #         if Solution.count == k: 
    #             print stringlist
    #             return
    #     for i in range(len(string)):
    #         self.dfs(n, k, string[:i]+string[i+1:], stringlist+string[i])

    # def getPermutation(self, n, k):
    #     string = ''
    #     for i in range(n): string += str(i+1)
    #     Solution.count = 0
    #     self.dfs(n, k, string, '')
    def getPermutation(self, n, k):
        res = ''
        k -= 1
        fac = 1
        for i in range(1, n): fac *= i
        num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in reversed(range(n)):
            curr = num[k/fac]
            res += str(curr)
            num.remove(curr)
            if i !=0:
                k %= fac
                fac /= i
        return res