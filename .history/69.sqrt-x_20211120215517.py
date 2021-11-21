#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] Sqrt(x)
#


# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        while left < right:
            mid = (right - left) / 2 + left


# @lc code=end
