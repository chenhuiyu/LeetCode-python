#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#


# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        # 方法1：辅助数组
        max_left = [0 for i in range(len(height))]
        max_right = [0 for i in range(len(height))]

        max_h = 0
        for i, h_i in enumerate(height):
            max_h = max(max_h, h_i)
            max_left[i] = max_h

        max_h = 0
        for i in range(len(height) - 1, -1, -1):
            max_h = max(max_h, height[i])
            max_right[i] = max_h

        sum = 0
        for i in range(len(height)):
            sum += max(0, min(max_left[i], max_right[i]) - height[i])
        return sum


# @lc code=end
