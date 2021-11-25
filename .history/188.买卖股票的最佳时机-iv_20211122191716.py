#
# @lc app=leetcode.cn id=188 lang=python3
#
# [188] 买卖股票的最佳时机 IV
#


# @lc code=start
class Solution:
    # 方法一：动态规划
    # def maxProfit(self, k: int, prices: List[int]) -> int:
    #     # 如果交易次数上限大于N/2，相当于无限次交易
    #     if k >= len(prices) / 2:
    #         sum = 0
    #         for i in range(1, len(prices)):
    #             if prices[i] > prices[i - 1]:
    #                 sum += prices[i] - prices[i - 1]
    #         return sum
    #     # 否则，动态规划
    #     else:
    #         # dp[i][j]表示在i位置做不超过k次交易的最大值
    #         # dp[0][:]全为0,dp[:][0]全为0
    #         dp = [[0 for j in range(k + 1)] for i in range(len(prices))]
    #         for i in range(len(prices)):
    #             for j in range(k + 1):
    #                 # i位置不做任何一次交易
    #                 dp[i][j] = dp[i - 1][j]
    #                 # i位置做最后一次交易的卖出操作
    #                 # 遍历最后一次交易的买入位置
    #                 for t in range(i):
    #                     dp[i][j] = max(dp[i][j], dp[t][j - 1] + prices[i] - prices[t])
    #         return dp[-1][-1]

    # 方法二：动态规划+斜率优化
    def maxProfit(self, k: int, prices: List[int]) -> int:

# @lc code=end
