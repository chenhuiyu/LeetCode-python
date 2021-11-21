#
# @lc app=leetcode.cn id=50 lang=python3
#
# [50] Pow(x, n)
#
n = 10
x = 2

x & 1


# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 0
        pow_n = x
        if n > 0:
            while n > 0:
                if n & 1 == 1:
                    print(ans)
                    ans *= pow_n
                n = n >> 1
                pow_n *= pow_n


# @lc code=end
