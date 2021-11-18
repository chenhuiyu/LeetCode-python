'''
Date: 2021-07-31 12:12:17
LastEditors: Chenhuiyu
LastEditTime: 2021-07-31 12:18:32
FilePath: \\LeetCodec:\\Users\\Administrator\\.leetcode\\11.盛最多水的容器.py
'''

#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#


# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left_Max_list = []
        left_Max = -1
        for i in range(len(height)):
            if height[i] > left_Max:
                left_Max = height[i]
            left_Max_list.append(left_Max)
        
        right_Max_list = []
        right_Max = -1
        for i in range(len(height)-1,0,-1):
            if height[i] > right_Max:
                right_Max=height[i]
            right_Max_list.append(right_Max)


# @lc code=end
