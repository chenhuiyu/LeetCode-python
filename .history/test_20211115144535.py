'''
Date: 2021-11-15 02:50:54
LastEditors: Chenhuiyu
LastEditTime: 2021-11-15 14:44:48
FilePath: \\.leetcode\\test.py
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def TreeNodeBuild(self, nums, low, high, count):
        if low > high:
            return None
        max_num = max(nums[low:high])
        max_index = nums[low:high].index(max_num)
        node = TreeNode(max_num)
        print(max_num, max_index)
        node.left = self.TreeNodeBuild(nums, low, max_index - 1)
        node.right = self.TreeNodeBuild(nums, max_index + 1, high)
        return node

    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        count = 0
        self.TreeNodeBuild(nums, 0, len(nums) - 1, count)


nums = [3, 2, 1, 6, 0, 5]
s = Solution()
s.constructMaximumBinaryTree(nums)
