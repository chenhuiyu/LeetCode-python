#
# @lc app=leetcode.cn id=50 lang=python3
#
# [50] Pow(x, n)
#
n = 5
x = 6


# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n > 0:
            while x > 0:
                if x & 1 == 1:
                    ans += pow
                x = x >> 1


# @lc code=end
