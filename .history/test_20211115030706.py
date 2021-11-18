'''
Date: 2021-11-15 02:50:54
LastEditors: Chenhuiyu
LastEditTime: 2021-11-15 03:07:06
FilePath: \\.leetcode\\test.py
'''
import heapq

lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
minHeap = []
for listi in lists:
    while listi:
        heapq.heappush(minHeap, listi.val)  #把listi中的数据逐个加到堆中
        listi = listi.next