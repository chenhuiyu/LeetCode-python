#
# @lc app=leetcode.cn id=50 lang=python3
#
# [50] Pow(x, n)
#
n = 5
x = 2


# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n > 0:
            while x > 0:
                x = x >> 1


# @lc code=end
