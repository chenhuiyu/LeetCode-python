#
# @lc app=leetcode.cn id=61 lang=python3
#
# [61] 旋转链表
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None: return None
        cur = head
        length = 0
        while cur.next is not None:
            cur = cur.next
            length += 1
        # 现在cur来到了尾结点的位置，记录尾结点
        length += 1
        tail = cur
        k = k % length
        # 双指针找到倒数第k个节点
        first = head
        second = head
        for i in range(k):
            second = second.next
        while second.next is not None:
            second = second.next
            first = first.next
        # first来到倒数第k个节点，这是我们要返回的链表的头结点
        # 将倒数第k-1个节点和第k个断开
        # 首尾相连


# @lc code=end
