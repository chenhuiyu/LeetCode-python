#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#


# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals, key=lambda x: x[0])
        start, end = None, None
        for interval in sorted_intervals:
            start_i, end_i = interval
            if start is None: start = start_i


# @lc code=end
