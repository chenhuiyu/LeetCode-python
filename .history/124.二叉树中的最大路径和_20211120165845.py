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
            if root.left is not None:
                left_max_path, left_head_path = loopInfo(root.left)
            else:
                left_max_path, left_head_path = None, None

            if root.right is not None:
                right_max_path, right_head_path = loopInfo(root.right)
            else:
                right_max_path, right_head_path = None, None

            # 更新root_head_path：必须以root为头
            if left_head_path is None and right_head_path is None:
                root_head_path = root.val
            elif left_head_path is None:
                root_head_path = max(root.val, right_head_path + root.val)
            elif right_head_path is None:
                root_head_path = max(root.val, left_head_path + root.val)
            else:
                root_head_path = max(
                    root.val,
                    left_head_path + root.val,
                    right_head_path + root.val,
                    left_head_path + right_head_path + root.val,
                )

            # 更新root_max_path:以root为头的最大路径和
            root_max_path = max(left_max_path, right_max_path, root_head_path)


# @lc code=end
