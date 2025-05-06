def buildArray(nums):
    """
    :type nums: List[int]
    :rtype: list[int]
    """
    ans = []

    for idx in range(len(nums)):
        val = nums[nums[idx]]
        ans.append(val)
    
    return ans

    #list comprehension: return [nums[nums[_]] for _ in range(len(nums))]