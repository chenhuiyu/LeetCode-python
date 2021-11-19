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
            max_left[i] = max(max_h, h_i)

        max_h = 0
        for i in range(len(height) - 1, -1, -1):
            max_right[i] = max(max_h, height[i])


# @lc code=end
