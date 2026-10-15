def two_sum_optimized(nums, target):
    if not nums:
        return []

    seen = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        
        if complement in seen:
            return [seen[complement],i]

        seen[num] = i
    
    return []



    
