def maxsubarray(nums):

    curr = max_sum = nums[0]

    for num in nums[1:]:
        curr = max(num, curr + num)
        max_sum = max(max_sum, curr)

    return max_sum

nums  = [-8, -3, -6, -2, -5]
print(maxsubarray(nums))


    