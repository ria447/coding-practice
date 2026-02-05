def thirdMax(nums):
        
        nums = list(set(nums))
        nums.sort()   
        length = len(nums)

        if length >= 3:
            return nums[-3]
    
        else:
            return max(nums)

nums = eval(input("enter the list:"))
output = thirdMax(nums)
print(output)
