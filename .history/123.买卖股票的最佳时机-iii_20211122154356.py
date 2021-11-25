#
# @lc app=leetcode.cn id=123 lang=python3
#
# [123] 买卖股票的最佳时机 III
#


# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        doneOnceMinusBuyMax = -prices[0]
        doneOncePrifit = 0
        minPriceUnitlI = prices[0]


# @lc code=end
