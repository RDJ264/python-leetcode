def searchInsert(nums,target):
    if target in nums:
        return nums.index(target)
    else:
        for items in nums:
            if items<target:
                firstindex=nums.index(items)
            else:
                break
        return firstindex+1

print(searchInsert([1,3,5,6],2))
print(searchInsert([1,3,5,6],7))
