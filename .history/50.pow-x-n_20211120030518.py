#
# @lc app=leetcode.cn id=50 lang=python3
#
# [50] Pow(x, n)
#
n = 5
x = 6

x & 1


# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 0
        pow_n = x
        if n > 0:
            while x > 0:
                if x & 1 == 1:
                    ans += pow_n
                x = x >> 1
                pow_n *= pow_n


# @lc code=end
