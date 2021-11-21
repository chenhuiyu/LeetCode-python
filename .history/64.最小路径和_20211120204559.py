#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#

# @lc code=start

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])

        dp=[[0 for i in range(m)] for j in range(n)]
        dp[0][0]=grid[0][0]

        for i range(1,m):
            dp[m][0]=dp[m-1][0]+grid[m][0]
        for j in range(1,n):
            dp[0][j]=dp[0][j-1]+grid[0][j]

        for i in range(2,m):
            for j in range(2,n):
                dp[i][j]=min(dp[i-1][j],dp[i][j-1])+grid[i][j]
        
        return dp[-1][-1]        
# @lc code=end

