#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#


# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 每个start，end对按照start位置排序
        sorted_intervals = sorted(intervals, key=lambda x: x[0])
        ans = []
        # 初始化start end
        start, end = sorted_intervals[0][0], sorted_intervals[0][1]
        # 遍历每一对
        for interval in sorted_intervals:
            start_i, end_i = interval
            # 如果当前的start_i>end，不在之前的范围内
            if start_i > end:
                # 收集上一组的start,end答案
                ans.append([start, end])
                # 另起炉灶
                start = start_i
                end = end_i
            # 如果当前end_i大于end，更新end值
            if end_i > end:
                end = end_i
        # 边界条件！添加最后一对
        ans.append([start, end])
        return ans


# @lc code=end
