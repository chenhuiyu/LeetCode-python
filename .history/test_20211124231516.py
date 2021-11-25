nums = [5, 1, 4, 2, 3, 4, 2, 2, 3]
pivot = 2
left = 0
right = len(nums) - 1

# pivot的值移到最右端
nums[pivot], nums[right] = nums[right], nums[pivot]
# nums[left:right-1] 根据nums[rigth]的值进行划分
target = nums[right]
# 小于区的右边界
lessRight = left - 1
# 大于区的左边界
moreLeft = right
# 循环控制变量，标记来到数组中的位置
i = left

while i < moreLeft:
    # 大于target
    if nums[i] > target:
        nums[i], nums[moreLeft - 1] = nums[moreLeft - 1], nums[i]
        moreLeft -= 1
    # 小于target
    elif nums[i] < target:
        nums[i], nums[lessRight + 1] = nums[lessRight + 1], nums[i]
        lessRight + 1
        i += 1
    else:
        i += 1

# right处的pivot移到大于区的左边界
nums[right], nums[moreLeft] = nums[moreLeft], nums[right]
print(nums)
print(lessRight + 1, moreLeft - 1)
