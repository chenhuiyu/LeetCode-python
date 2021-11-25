#
# @lc app=leetcode.cn id=188 lang=python3
#
# [188] 买卖股票的最佳时机 IV
#

# @lc code=start
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # 如果交易次数上限大于N/2，相当于无限次交易
        if k>=len(prices)/2:
            sum=0
            for i in range(len(prices)):
                if prices[i]>prices[i-1]:
# @lc code=end

