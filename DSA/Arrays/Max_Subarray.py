def maxsubarray(nums):
    if not nums:
        return []

    max_sum = curr = nums[0]

    for i in nums[1:]:
        curr = max(curr, curr + num)
        max_sum = max(max_sum, curr)

    return max_sum