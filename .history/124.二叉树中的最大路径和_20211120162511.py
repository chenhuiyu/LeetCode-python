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
            if root is None:
                return 0
            left_max = loopInfo(root.left) if root.left is not None else 0
            right_max = loopInfo(root.right) if root.right is not None else 0
            if root.left is None and root.right is None:
                root_max = root.val
            elif root.left is None:
                root_max = max(root.val, right_max, root.val + right_max)
            elif root.right is None:
                root_max = max(root.val, left_max, root.val + left_max)
            else:
                root_max = max(left_max, right_max, root.val, left_max + root.val, right_max + root.val, left_max + right_max + root.val)
            return root_max

        return loopInfo(root)


# @lc code=end
