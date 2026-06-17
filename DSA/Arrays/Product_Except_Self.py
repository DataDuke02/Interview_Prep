def productExceptSelf(nums):
    if not nums:
        return []

    n = len(nums)
    result = [1]*n

    left_product = 1
    for i in range(n):
        result[i] = left_product
        left_product *= nums[i]

    right_product = 1
    for i in range(n-1, -1, -1):
        result[i] = right_product
        left_product *= nums[i]

    return result