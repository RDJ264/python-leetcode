def searchrange(nums,target):
    flag=0
    count=0
    positions=[]
    for i in nums:
        if i==target:
            flag=1
            positions.append(nums.index(target,nums.index(target)+count,len(nums)))
            count+=1
    if flag==0:
        return [-1,-1]
    return positions


print(searchrange([5,7,7,8,8,10],8))
print(searchrange([5,7,7,8,8,10],6))
print(searchrange([],0))            
print(searchrange([2,2],2))            
