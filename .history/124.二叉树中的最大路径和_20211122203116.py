#
# @lc app=leetcode.cn id=124 lang=python3
#
# [124] 二叉树中的最大路径和
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def loopInfo(root):
            # 返回两个值，以root为头的最大路径和，包含root的最大路径和
            if root is None: return 0, 0
            maxPathSumFromHeadLeft,maxPathSumLeft=loopInfo(root.left) is root.left is not None else 0,float("-inf")
            maxPathSumFromHeadRight,maxPathSumRight=loopInfo(root.right) is root.right is not None else 0,float("-inf")
            maxPathSumFromHead=max(maxPathSumFromHeadLeft+root.val,maxPathSumFromHeadRight+root.val)

            maxPathSum=max(maxPathSumLeft,maxPathSumRight,root.val,maxPathSumFromHead,maxPathSumFromHeadLeft+root,val+maxPathSumFromHeadLeft+)

            
        return loopInfo(root)[0]


# @lc code=end
