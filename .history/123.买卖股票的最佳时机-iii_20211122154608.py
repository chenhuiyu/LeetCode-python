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

        for i in range(len(prices)):
            minPriceUnitlI = min(minPriceUnitlI, prices[i])
            doneOncePrifit = max(doneOncePrifit, prices[i] - minPriceUnitlI)
            doneOnceMinusBuyMax = max(doneOnceMinusBuyMax, doneOncePrifit - prices[i])
            ans = max(doneOnceMinusBuyMax + prices[i], abs)


# @lc code=end
