'''
Date: 2021-11-16 17:05:49
LastEditors: Chenhuiyu
LastEditTime: 2021-11-16 19:01:50
FilePath: \\.leetcode\\333.最大BST子树.py
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        def loopInfo(root):
            # 以root为根的子树返回四个信息：最大BST子树的大小、是否是搜索二叉树，整棵树的最大值、整棵树的最小值
            if root is None:
                return 0, True, float("-inf"), float("inf")
            left_bst_size, left_isBST, left_max, left_min = loopInfo(root.left)
            right_bst_size, right_isBST, right_max, right_min = loopInfo(root.right)

            # 判断当前root子树是否是搜索二叉树
            # 条件：左子树是搜索二叉树，右子树是搜索二叉树，左子树最大值小于root.val，右子树最小值大于root.val
            if left_isBST is True and right_isBST is True and left_max < root.val and right_min > root.val:
                root_isBst = True
            else:
                root_isBst = False

            # 更新以root为根的子树的最大值
            root_max = max(root.val, left_max, right_max)
            # 更新以root为根的子树的最小值
            root_min = min(root.val, left_min, right_min)

            # 以root为根的子树最大BST子树的大小
            if root_isBst == True:
                # 左子树整体都是BST，左子树的节点个数就是left_bst_size，右子树同理
                root_bst_size = left_bst_size + right_bst_size + 1
            else:
                root_bst_size = max(left_bst_size, right_bst_size)
            return root_bst_size, root_isBst, root_max, root_min

        return loopInfo(root)[0]