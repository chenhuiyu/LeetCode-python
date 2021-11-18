'''
Date: 2021-11-15 14:58:10
LastEditors: Chenhuiyu
LastEditTime: 2021-11-15 14:59:33
FilePath: \\.leetcode\\654.最大二叉树.py
'''
#
# @lc app=leetcode.cn id=654 lang=python3
#
# [654] 最大二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 辅助函数
    def build(self,nums,low,high):
        # 找到nums[low:high]中的最大值，作为root节点
        max_nums=max(nums[low:high])
    # 主函数
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:

# @lc code=end

