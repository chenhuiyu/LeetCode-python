class Solution:
    def maxSubArray(self, nums: List[int]) -> int
        left=0
        right=left
        summax=0
        while right<len(nums):
            summax+=nums[right]
            if summax<=0:
                summax=0
                left=right+1
                right=left
            else:
                right+=1
        return summax