#
# @lc app=leetcode.cn id=687 lang=python3
#
# [687] 最长同值路径
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        def loopInfo(root):
            # 以root为头结点的数的递归，返回两个值
            # longestPath:以root为头结点的当前最长同值路径的长度
            # sameRootVal:和root.val同值的路径的长度
            if root is None:
                return 0, 0

            leftLongestPath, leftSameRootVal = loopInfo(root.left)
            rightLongestPath, rightSameRootVal = loopInfo(root.right)

            # 如果root.val和左右子树的值都不同
            if root.val != root.left.val and root.val != root.right.val:
                sameRootVal = 1
            # 如果和左右子树中的一个值相同
            elif root.val == root.left.val and root.val != root.right.val:
                sameRootVal = leftSameRootVal + 1
            elif root.val == root.right.val and root.val != root.left.val:
                sameRootVal = rightSameRootVal + 1
            else:
                sameRootVal = leftSameRootVal + rightSameRootVal + 1

            # 最长同值路径等于左右子树的最长同值路径和sameRootVal三者取最大
            longestPath = max(leftLongestPath, rightLongestPath, sameRootVal)


# @lc code=end
