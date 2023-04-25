def twosum(nums,target):
    i=0
    s=0
    number=[]
    while i<len(nums):
       j=i+1
       while j<len(nums):
           if nums[i]+nums[j]==target:
               number.append(i)
               number.append(j)
           j+=1
       i+=1
    return number

print(twosum([2,7,11,15],9))
print(twosum([3,2,4],6))
print(twosum([3,3],6))
