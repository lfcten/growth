def rob(nums):
    if not nums:
        return 0
    n = len(nums)
    if n == 1:
        return nums[0]

    pre_max = nums[0]
    cur_max = max(pre_max, nums[1])
    for i in range(2, n):
        temp = max(pre_max + nums[i], cur_max)
        pre_max = cur_max
        cur_max = temp
    return cur_max


print(rob([5, 1, 1, 5]))
