def partition(nums, left, right, pivot):
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
        if i > target:
            nums[i], nums[moreLeft - 1] = nums[moreLeft - 1], nums[i]
            moreLeft -= 1
        # 小于target
        elif nums[i] < target:
            nums[i], nums[lessRight + 1] = nums[lessRight + 1], nums[i]
            lessRight += 1
            i += 1
        else:
            i += 1

    # right处的pivot移到大于区的左边界
    nums[right], nums[moreLeft] = nums[moreLeft], nums[right]
    return lessRight + 1, moreLeft - 1


nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
partition(nums, 0, len(nums) - 1, 1)
