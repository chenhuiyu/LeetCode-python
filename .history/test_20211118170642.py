nums = [1, 4, 5, 5, 5, 7, 8]
target = 5
left = 0
right = len(nums) - 1
max_right = -1
while left < right:
    mid = (left + right) // 2
    # 中点小于target，在右侧二分(找最右)
    if nums[mid] <= target:
        # 中点处等于target
        # 用mid值更新min_left
        if nums[mid] == target:
            max_right = mid
        # 右侧二分
        left = mid + 1
    # 中点大于target：在左侧二分:
    if nums[mid] > target:
        right = mid - 1