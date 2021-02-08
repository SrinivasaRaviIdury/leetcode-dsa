def onedrunningsum(nums):
    l = [None] * len(nums)
    if len(nums) == 0:
        return l
    l[0] = nums[0]
    for i in range(1,len(nums)):
        l[i] = l[i-1] + nums[i]
    return l

nums=[3,4,5,6]
newnums=onedrunningsum(nums)
print(newnums)