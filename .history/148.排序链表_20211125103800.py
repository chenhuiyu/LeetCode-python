#
# @lc app=leetcode.cn id=148 lang=python3
#
# [148] 排序链表
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge(self, head1, head2):
        dummyHead = ListNode()
        p1 = head1
        p2 = head2
        cur = dummyHead
        while p1 is not None and p2 is not None:
            if p1.val > p2.val:
                cur.next = p2

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 求得整个链表的长度
        cur = head
        length = 0
        while cur is not None:
            cur = cur.next
            length += 1


# @lc code=end
