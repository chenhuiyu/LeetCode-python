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
        less_close = 0
        while left < right:

            mid = (right - left) // 2 + left
            # print("left:", left, " mid:", mid, " right:", right)
            if mid * mid == x:
                print("Solution:", mid)
                break
                # return mid
            if mid * mid > x:
                right = mid - 1
            else:
                less_close = mid
                left = mid + 1
        return less_close


# @lc code=end
