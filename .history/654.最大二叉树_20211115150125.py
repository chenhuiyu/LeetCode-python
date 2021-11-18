'''
Date: 2021-11-15 14:58:10
LastEditors: Chenhuiyu
LastEditTime: 2021-11-15 15:01:25
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
        # 记录最大值的下标index，作为划分左子树和右子树的分隔
        max_index=nums.index(max_nums)
        root=TreeNode(max_nums)
        # 左子树是通过数组中 最大值左边部分 递归构造出的最大二叉树
    # 主函数
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:

# @lc code=end

