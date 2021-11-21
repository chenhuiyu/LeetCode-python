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
            if root.val != left_val and root.val != right_val:
                sameRootVal = 1
            # 如果只向左树延伸
            if root.val == left_val:
                sameRootValOnlyLeft = leftSameRootVal + 1
            # 如果只向右树延伸
            if root.val == right_val:
                sameRootValOnlyRight = rightSameRootVal + 1
            sameRootVal = max()

            # 最长同值路径等于左右子树的最长同值路径和sameRootVal三者取最大
            longestPath = max(leftLongestPath, rightLongestPath, sameRootVal)
            return longestPath, sameRootVal

        # 根据题目条件，同值的路径的长度等于节点数减一
        return loopInfo(root)[0] - 1


[1, null, 1, 1, 1, 1, 1, 1]

# @lc code=end
