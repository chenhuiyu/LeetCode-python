'''
Date: 2021-11-15 02:50:54
LastEditors: Chenhuiyu
LastEditTime: 2021-11-15 02:52:00
FilePath: \\.leetcode\\test.py
'''
import heapq

list = [1, 2, 4, 5, 2, 6, 3, 7, 3, 2, 6]

minheap = heapq.heapify(list)
minheap.heappop()